import json
from main import con
from export_csv import TABLES

data = {}

with con:

    cur = con.cursor()

    for table in TABLES:
        cur.execute('select * from ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

    for row in cur:
        rows.append(dict(zip(fields, row)))

    data[table] = rows

    with open('all_data.json', 'w') as outf:
        json.dump(data, outf, default=str)


