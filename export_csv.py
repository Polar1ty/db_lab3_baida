import csv
from main import con

OUTPUT_FILE_T = 'exported_DB_{}.csv'

TABLES = [
    'sportsman',
    'games',
    'sportsman_games',
    'sport',
    'sportsman_sport',
]

with con:
    cur = con.cursor()

    for table_name in TABLES:
        cur.execute('select * from ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])
