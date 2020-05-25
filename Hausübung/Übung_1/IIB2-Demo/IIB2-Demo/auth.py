
import functools
import databasemanager

from flask import (
	Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint("auth", "auth", url_prefix="/auth")

def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view




@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("application.index"))




@bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None
        user = databasemanager.getBauleiterLogin(username)
        password_db = user[4]
        print (user)
        if password_db is None:
            error = "Incorrect username."
       # elif not check_password_hash(password_db, password): must register first
        elif not password_db == password:
            error = "Incorrect password."
            print(error = "Incorrect password.")

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = user[0]
            return redirect(url_for("application.index"))
        flash(error)
    return render_template("/login.html")


@bp.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user.
    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        # elif (
        # db.execute("SELECT id FROM user WHERE username = ?", (username,)).fetchone()
        # is not None
        # ):
        #   error = "User {0} is already registered.".format(username)

        if error is None:
            # the name is available, store it in the database and go to
            # the login pag
            databasemanager.insertBauleiter(username, generate_password_hash(password))
            return redirect(url_for("auth.login"))
        flash(error)
    return render_template("/register.html")




