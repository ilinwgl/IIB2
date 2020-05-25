import functools
import databasemanager
from auth import login_required

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
        sql_query = "select geb_id, geb_plz, geb_strasse, geb_hausnummer,geb_ort from gebaeude where geb_blt_id = " + str(id)
        records = databasemanager.getAll(sql_query)
        return render_template("/index.html", records = records)
    else:
        return render_template("/index.html")


@bp.route("/stockwerk", methods=("POST",) )
@login_required
def stockwerk():
    """Show all the buildings"""

    if (session.get("user_id") != None):
        id = request.form["stockwerk_id"]
        sql_query = "select * from stockwerk where stw_geb_id = " + str(id)
        stocks = databasemanager.getAll(sql_query)
        return render_template("/stockwerk.html", stocks = stocks)
    else:
        return render_template("/index.html")


@bp.route('/postjson', methods=['POST'])
def postJsonHandler():
    print(request.is_json)
    content = request.get_json()
    time = str(content["time"])
    field = content["field"]
    value = content["value"]
    sql_insert = "INSERT INTO datable (logdate, field, value) VALUES (%s,%s,%s)"
    insert_tuple = (time,field,value)
    print(sql_insert)
    databasemanager.insertData(sql_insert,insert_tuple)

    print(content)
    return 'JSON posted'