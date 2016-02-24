import os
import psycopg2
import urlparse
import uuid

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)


def create_user(user):
    cursor = conn.cursor()
    user_uuid = str(uuid.uuid4())
    query = "INSERT INTO users (name, email, password, uuid) VALUES (%s, %s, %s, %s);"  # noqa
    data = (user.name, user.email, user.password, user_uuid)

    cursor.execute(query, data)
    conn.commit()
    return user_uuid


def get_user(user):
    cursor = conn.cursor()
    query = "SELECT uuid FROM users WHERE email=%s and password=%s"
    data = (user.email, user.password)

    cursor.execute(query, data)
    rows = cursor.fetchall()

    return rows


def get_scenarios_for_user(uuid):
    cursor = conn.cursor()
    query = "SELECT * FROM requests WHERE userid=%s"
    data = uuid

    cursor.execute(query, data)
    rows = cursor.fetchall()

    return rows
