from ping3 import ping
from db import connect
from datetime import datetime

db = connect()

cursor = db.cursor()

cursor.execute(

"SELECT id, ip_address FROM devices"

)

devices = cursor.fetchall()

for device in devices:

    id = device[0]

    ip = device[1]

    response = ping(ip)

    if response:

        status = "ONLINE"

        response = response * 1000

    else:

        status = "OFFLINE"

        response = 0

        alert_sql = """

INSERT INTO alerts

(device_id, message, created_at)

VALUES(%s,%s,%s)

"""

        msg = f"{ip} is DOWN"

        cursor.execute(

            alert_sql,

            (

                id,

                msg,

                datetime.now()

            )

        )

    sql = """

UPDATE devices

SET status=%s,

response_time=%s,

last_checked=%s

WHERE id=%s

"""

    values = (

        status,

        response,

        datetime.now(),

        id

    )

    cursor.execute(sql, values)

db.commit()

print("Monitoring Complete")