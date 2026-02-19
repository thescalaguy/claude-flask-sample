import datetime

from peewee import AutoField, DateTimeField, FloatField, Model
from playhouse.pool import PooledPostgresqlDatabase

db = PooledPostgresqlDatabase(
    "postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port=5432,
    max_connections=8,
    stale_timeout=300,
)


class Addition(Model):
    id = AutoField()
    a = FloatField()
    b = FloatField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Quotient(Model):
    id = AutoField()
    a = FloatField()
    b = FloatField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Subtraction(Model):
    id = AutoField()
    a = FloatField()
    b = FloatField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
