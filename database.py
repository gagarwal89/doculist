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
    query = "INSERT INTO users (name, email, password, uuid) VALUES (%s, %s, %s, %s);"  # noqa
    data = (user.name, user.email, user.password, str(uuid.uuid4()))

    cursor.execute(query, data)
    conn.commit()


def get_user(user):
    cursor = conn.cursor()
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s);"
    data = (user.name, user.email, user.password)

    cursor.execute(query, data)
    conn.commit()
