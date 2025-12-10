#!/usr/bin/env python3
"""
PandAuth models

@author:
@version: 2025.12
"""

import datetime

from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime

from . import db, mm


# SQLAlchemy model
class User(UserMixin, db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    google_id: Mapped[str] = mapped_column(String(), unique=True, nullable=True)
    username: Mapped[str] = mapped_column(String(), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(), unique=True, nullable=False)
    picture: Mapped[str] = mapped_column(String(), nullable=True)
    password_hash: Mapped[str] = mapped_column(String(), nullable=False, default="")
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)


# Marshmallow schema
class UserSchema(mm.SQLAlchemyAutoSchema):
    """User schema"""

    class Meta:
        """Metadata"""
        model = User
        include_relationships = True
        load_instance = True
