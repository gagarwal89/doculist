import os
import psycopg2
import urlparse

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
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s);"
    data = (user.name, user.email, user.password)

    cursor.execute(query, data)
    conn.commit()
