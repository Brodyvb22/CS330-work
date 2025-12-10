#!/usr/bin/env python3
"""
PandAuth authentication

@author:
@version: 2025.12
"""

import datetime
import json

import requests
from flask import Blueprint, current_app, redirect, request, url_for
from flask_login import login_required, login_user, logout_user

from . import client, db, login_manager
from .models import User

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.get("/login")
def login():
    """Log in"""
    google_config = current_app.config["GOOGLE_CONFIG"]
    authorization_endpoint = google_config["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=url_for("auth.callback", _external=True),
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)



@auth.route("/login/callback")
def callback():
    """Google callback"""
    code = request.args.get("code")

    google_config = current_app.config["GOOGLE_CONFIG"]
    token_endpoint = google_config["token_endpoint"]


    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=url_for("auth.callback", _external=True),
        code=code,
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(
            current_app.config["GOOGLE_CLIENT_ID"],
            current_app.config["GOOGLE_CLIENT_SECRET"],
        ),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    #Get user info
    userinfo_endpoint = google_config["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    userinfo = userinfo_response.json()

    google_id = userinfo.get("sub")
    email = userinfo.get("email")
    name = userinfo.get("name", email)
    picture = userinfo.get("picture")


    user = db.session.query(User).filter_by(email=email).first()
    if not user:
        user = User(
            google_id=google_id,
            username=name,
            email=email,
            picture=picture,
            password_hash="",
            created_at=datetime.datetime.utcnow(),
        )
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(url_for("main.index"))


@auth.route("/logout")
@login_required
def logout():
    """Log out"""
    logout_user()
    return redirect(url_for("main.index"))


@login_manager.user_loader
def load_user(user_id):
    """User loader"""
    return db.session.query(User).filter_by(id=user_id).first()