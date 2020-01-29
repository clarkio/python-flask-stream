from functools import wraps

from flask import g, redirect, request, session, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = session.get('username', '')
        if not "username" in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function
