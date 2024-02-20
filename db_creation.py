import psycopg2

conn = psycopg2.connect("")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS""")

conn.commit()
cur.close()
conn.close()