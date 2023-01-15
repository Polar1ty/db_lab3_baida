import csv
from main import con

INPUT_CSV_FILE = 'athlete_events.csv'

query_create_new_table = '''
create table games_copy as select * from games
'''

query_delete = '''
delete from games_copy
'''

query_insert = '''
insert into games_copy (games_name, games_year, games_city) values (%s, %s, %s)
'''

with con:
    cur = con.cursor()
    cur.execute(query_create_new_table)
    cur.execute(query_delete)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            values = (row['Games'], row['Year'], row['City'])
            cur.execute(query_insert, values)

    con.commit()
