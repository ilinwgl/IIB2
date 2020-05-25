import functools
import databasemanager
from auth import login_required
import datetime

from flask import (
	Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for, )

bp = Blueprint("application", "application")

@bp.route("/index")
@login_required
def index():
    """Show all the buildings"""

    if (session.get("user_id") != None):
        id = session.get("user_id")
        sql_query = "select ge_id, ge_name, ge_ort, ge_plz, ge_strasse, ge_hausnummer from gebaeude, personen, ln_datenbearbeiten where ln_dabe_per_id = "+ str(id) +" AND ln_dabe_ge_id = ge_id"
        records = databasemanager.getAll(sql_query)
        return render_template("/index.html", records = records)
    else:
        return render_template("/index.html")


@bp.route("/stockwerk", methods=("POST",) )
@login_required
def stockwerk():
    """Show all the Stockwerk"""

    if (session.get("user_id") != None):
        id = request.form["stockwerk_id"]
        sql_query = "select sw_id, sw_bezeichnung from Stockwerk where sw_ge_id = " + str(id)
        stocks = databasemanager.getAll(sql_query)
        return render_template("/stockwerk.html", stocks = stocks)
    else:
        return render_template("/index.html")


@bp.route("/raum", methods=("POST",) )
@login_required
def raum():
    """Show all the rooms"""

    if (session.get("user_id") != None):
        id = request.form["raum_id"]
        sql_query = "select ra_id, ra_bezeichnung, ra_nummer, ra_ifc_guid from Raum where ra_sw_id = " + str(id)
        raums = databasemanager.getAll(sql_query)
        return render_template("/raum.html", raums = raums)
    else:
        return render_template("/index.html")


@bp.route("/HAVC", methods=("POST",) )
@login_required
def HAVC():
    """Show all the HAVCs"""

    if (session.get("user_id") != None):
        id = request.form["HAVC_id"]       
        sql_query = "select havc_id, havc_name, havc_typ, havc_position, havc_sw_id from havc where havc_sw_id = " + str(id)
        HAVCs = databasemanager.getAll(sql_query)

        return render_template("/HAVC.html", HAVCs = HAVCs)
    else:
        return render_template("/index.html")


@bp.route("/wand", methods=("POST",) )
@login_required
def wand():
    """Show all the wands"""


    if (session.get("user_id") != None):
        id = request.form["wand_id"]
        s = session.get("id")
        print(s)

        sql_query = "select wa_id, wa_schaden, ln_bes_wa_richtung, wa_ifc_guid from wand, ln_besitzen where ln_bes_ra_id = " +str(id)+ " and ln_bes_wa_id = wa_id"
        wands = databasemanager.getAll(sql_query)
        return render_template("/wand.html", wands = wands)
    else:
        return render_template("/index.html")


@bp.route("/sensor", methods=("POST",) )
@login_required
def sensor():
    """Show all the sensors"""

    if (session.get("user_id") != None):
        id = request.form["sensor_id"]
        sql_query = "select sen_id, sen_name, sen_typ, sen_position, sen_ra_id from Sensor where sen_ra_id = " + str(id)
        sens = databasemanager.getAll(sql_query)
        return render_template("/sensor.html", sens = sens)
    else:
        return render_template("/index.html")


@bp.route("/raumbearbeiten", methods=("POST",) )
@login_required
def raumbearbeiten():

    if (session.get("user_id") != None):
        id = request.form["bearbeiten"]
        sql_query = "select ra_id, ra_bezeichnung, ra_nummer, ra_sw_id, ra_ifc_guid from raum where ra_id = " + str(id)
        raum = databasemanager.getOne(sql_query)
        return render_template("/raumbearbeiten.html", raum = raum)
    else:
        return render_template("/index.html")


@bp.route("/raumspeichern", methods=("POST",) )
@login_required
def raumspeichern():

    if (session.get("user_id") != None):

        id = request.form["speichern"]
        bezeichnung = request.form["bezeichnung"]
        nummer = request.form["nummer"]
        ebene = request.form["stockwerk"]
        ifc_guid = request.form["ifc_guid"]

        databasemanager.updateTable("raum", "ra_bezeichnung", bezeichnung, "ra_id", id)
        databasemanager.updateTable("raum", "ra_nummer", nummer, "ra_id", id)
        databasemanager.updateTable("raum", "ra_sw_id", ebene, "ra_id", id)
        databasemanager.updateTable("raum", "ra_ifc_guid", ifc_guid, "ra_id", id)

        sql_query = "select ra_id, ra_bezeichnung, ra_nummer, ra_ifc_guid from raum where ra_sw_id = " + str(ebene)
        raums = databasemanager.getAll(sql_query)
        return render_template("/raum.html", raums = raums)
    else:
        return render_template("/index.html")


@bp.route("/wandbearbeiten", methods=("POST",) )
@login_required
def wandbearbeiten():

    if (session.get("user_id") != None):
        id = request.form["bearbeiten"]

        sql_query = "select wa_id, wa_schaden, ln_bes_ra_id, wa_ifc_guid from wand, ln_besitzen where wa_id = " + str(id) + " and wa_id = ln_bes_wa_id"
        wand = databasemanager.getOne(sql_query)
        return render_template("/wandbearbeiten.html", wand = wand)
    else:
        return render_template("/index.html")


@bp.route("/wandspeichern", methods=("POST",) )
@login_required
def wandspeichern():

    if (session.get("user_id") != None):
        ra_id = request.form["speichern"]
        id = request.form["id"]
        schaden = request.form["schaden"]

        databasemanager.updateTable("wand", "wa_schaden", schaden, "wa_id", id)
        sql_query = "select wa_id, wa_schaden, ln_bes_wa_richtung, wa_ifc_guid from wand, ln_besitzen where ln_bes_ra_id = " +str(ra_id)+ " and ln_bes_wa_id = wa_id"
        wands = databasemanager.getAll(sql_query)
        return render_template("/wand.html", wands = wands)
    else:
        return render_template("/index.html")


@bp.route("/HAVCadd", methods=("POST",) )
@login_required
def havcadd():
    """Add a new Sensor"""
    if (session.get("user_id") != None):

        sql_query = "select sw_id from stockwerk"
        stocks = databasemanager.getAll(sql_query)
        return render_template("/HAVCadd.html", stocks = stocks)
    else:
        return render_template("/index.html")


@bp.route("/havcnew", methods=("POST",) )
@login_required
def havcnew():

    if (session.get("user_id") != None):
        name = request.form["name"]
        typ = request.form["typ"]
        position = request.form["position"]
        ebene = request.form["stockwerk"]

        sql_query = "insert into havc (havc_name, havc_typ, havc_position, havc_sw_id) values (%s, %s, %s, %s)"
        insert_tuple = (name, typ, position, ebene)
        databasemanager.insertData(sql_query, insert_tuple)

        sql_query_select = "select havc_id, havc_name, havc_typ, havc_position, havc_sw_id from havc where havc_sw_id = " + str(ebene)
        HAVCs = databasemanager.getAll(sql_query_select)
        return render_template("/HAVC.html", HAVCs = HAVCs)
    else:
        return render_template("/index.html")


@bp.route("/havcbearbeiten", methods=("POST",) )
@login_required
def havcbearbeiten():

    if (session.get("user_id") != None):
        id = request.form["bearbeiten"]
        sql_query = "select havc_id, havc_name, havc_typ, havc_position, havc_sw_id from havc where havc_id = " + str(id)
        HAVC = databasemanager.getOne(sql_query)
        return render_template("/HAVCbearbeiten.html", HAVC = HAVC)
    else:
        return render_template("/index.html")


@bp.route("/havcspeichern", methods=("POST",) )
@login_required
def havcspeichern():

    if (session.get("user_id") != None):
        id = request.form["speichern"]
        name = request.form["name"]
        typ = request.form["typ"]
        position = request.form["position"]
        ebene = request.form["ebene"]

        databasemanager.updateTable("havc", "havc_name", name, "havc_id", id)
        databasemanager.updateTable("havc", "havc_typ", typ, "havc_id", id)
        databasemanager.updateTable("havc", "havc_position", position, "havc_id", id)
        databasemanager.updateTable("havc", "havc_sw_id", ebene, "havc_id", id)

        sql_query = "select havc_id, havc_name, havc_typ, havc_position, havc_sw_id from havc where havc_sw_id = " + str(ebene)
        HAVCs = databasemanager.getAll(sql_query)
        return render_template("/HAVC.html", HAVCs = HAVCs)
    else:
        return render_template("/index.html")


@bp.route("/havcdelete", methods=("POST",) )
@login_required
def havcdelete():

    if (session.get("user_id") != None):
        id = request.form["havc_entfernen"]
        databasemanager.deletedata("havc", "havc_id", id)

        stockwerk = request.form["stockwerk"]
        sql_query = "select havc_id, havc_name, havc_typ, havc_position, havc_sw_id from havc where havc_sw_id = " + str(stockwerk)
        HAVCs = databasemanager.getAll(sql_query)
        return render_template("/HAVC.html", HAVCs = HAVCs)
    else:
        return render_template("/index.html")


@bp.route("/sensoradd", methods=("POST",) )
@login_required
def sensoradd():
    """Add a new Sensor"""
    if (session.get("user_id") != None):

        sql_query_raum = "select ra_id, ra_bezeichnung, ra_nummer from raum"
        raums = databasemanager.getAll(sql_query_raum)
        sql_query_havc = "select havc_id, havc_name from havc"
        havcs = databasemanager.getAll(sql_query_havc)
        return render_template("/sensoradd.html", raums = raums, havcs = havcs)
    else:
        return render_template("/index.html")


@bp.route("/sensornew", methods=("POST",) )
@login_required
def sensornew():

    if (session.get("user_id") != None):
        name = request.form["name"]
        typ = request.form["typ"]
        position = request.form["position"]
        raum = request.form["raum"]
        havc = request.form["havc"]

        sql_query = "insert into sensor (sen_name, sen_typ, sen_position, sen_ra_id, sen_havc_id) values (%s, %s, %s, %s, %s)"
        insert_tuple = (name, typ, position, raum, havc)
        databasemanager.insertData(sql_query, insert_tuple)

        sql_query_select = "select sen_id, sen_name, sen_typ, sen_position from sensor where sen_ra_id = " + str(raum)
        sens = databasemanager.getAll(sql_query_select)
        return render_template("/sensor.html", sens = sens)
    else:
        return render_template("/index.html")


@bp.route("/sensorbearbeiten", methods=("POST",) )
@login_required
def sensorbearbeiten():

    if (session.get("user_id") != None):
        id = request.form["bearbeiten"]
        sql_query = "select sen_id, sen_name, sen_typ, sen_position, sen_ra_id, sen_havc_id from sensor where sen_id = " + str(id)
        sen = databasemanager.getOne(sql_query)
        return render_template("/sensorbearbeiten.html", sen = sen)
    else:
        return render_template("/index.html")


@bp.route("/sensorspeichern", methods=("POST",) )
@login_required
def sensorspeichern():

    if (session.get("user_id") != None):
        id = request.form["speichern"]
        name = request.form["name"]
        typ = request.form["typ"]
        position = request.form["position"]
        raum = request.form["raum"]
        havc = request.form["havc"]

        databasemanager.updateTable("sensor", "sen_name", name, "sen_id", id)
        databasemanager.updateTable("sensor", "sen_typ", typ, "sen_id", id)
        databasemanager.updateTable("sensor", "sen_position", position, "sen_id", id)
        databasemanager.updateTable("sensor", "sen_ra_id", raum, "sen_id", id)
        databasemanager.updateTable("sensor", "sen_havc_id", havc, "sen_id", id)

        sql_query = "select sen_id, sen_name, sen_typ, sen_position, sen_ra_id, sen_havc_id from sensor where sen_ra_id = " + str(raum)
        sens = databasemanager.getAll(sql_query)
        return render_template("/sensor.html", sens = sens)
    else:
        return render_template("/index.html")


@bp.route("/sensordelete", methods=("POST",) )
@login_required
def sensordelete():

    if (session.get("user_id") != None):
        id = request.form["sen_entfernen"]
        databasemanager.deletedata("sensor", "sen_id", id)

        raum = request.form["raum"]
        sql_query = "select sen_id, sen_name, sen_typ, sen_position, sen_ra_id from sensor where sen_ra_id = " + str(raum)
        sens = databasemanager.getAll(sql_query)
        return render_template("/sensor.html", sens = sens)
    else:
        return render_template("/index.html")


@bp.route("/stockwerkcheck", methods=("POST",) )
@login_required
def stockwerkcheck():
    if (session.get("user_id") != None):
        tem_grenze = float(request.form["temperaturgrenze"])
        feu_grenze = float(request.form["feuchtigkeitsgrenze"])

        sql_query1 = "select seda_id, seda_zeit, seda_temperatur, seda_feuch, seda_sen_id from sensordaten"
        sendas = databasemanager.getAll(sql_query1)

        for senda in sendas:
            timestamp = senda[1]
            sql_query3 = "select sen_havc_id from sensor, sensordaten where seda_id = " + str(senda[0]) + " and seda_sen_id = sen_id" 
            havc_id = databasemanager. getOne(sql_query3)
            if (tem_grenze < senda[2] <  2 * tem_grenze or feu_grenze < senda[3] <   2 * feu_grenze):
                status = "An"
                stuf = "Stufe 1"
            elif(2 * tem_grenze < senda[2] < 3 *  tem_grenze or 2 * feu_grenze < senda[3] < 3 * feu_grenze):
                status = "An"
                stuf = "Stufe 2"
            elif(senda[2] > 3 *  tem_grenze or senda[3] > 3 * feu_grenze):
                status = "An"
                stuf = "Stufe 3"
            else:
                status = "Aus"
                stuf = "Stufe 0"
            sql_query2 = """insert into havcdaten (havcda_zeitpunkt, havcda_stufe, havcda_AnAusStatus, havcda_havc_id)
                            values (%s, %s, %s, %s)"""
            insert_tuple = (timestamp, stuf, status, havc_id[0])
            databasemanager.insertData(sql_query2, insert_tuple)

        sql_query4 = "select * from havcdaten"
        havcdatens = databasemanager.getAll(sql_query4)
        return render_template("/stockwerkcheck.html", havcdatens = havcdatens)
    else:
        return render_template("/index.html")



@bp.route('/postjson', methods=['POST'])
def postJsonHandler():
    print(request.is_json)
    content = request.get_json()
    temp = content["temp"]
    feuch = content["feuch"]
    timestamp = datetime.datetime.now()
    sen_id = 1

    sql_insert = """INSERT INTO sensordaten (seda_zeit, seda_temperatur, seda_feuch, seda_sen_id) 
                 VALUES (%s,%s,%s,%s)"""
    insert_tuple = (timestamp,temp,feuch,sen_id)
    print(sql_insert)
    databasemanager.insertData(sql_insert,insert_tuple)

    print(content)
    return 'JSON posted'
