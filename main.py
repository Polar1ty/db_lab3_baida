import psycopg2
import matplotlib.pyplot as plt


username = 'postgres'
password = '123123'
database = 'postgres'
host = 'localhost'
port = '5432'

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

query_1 = '''
create view SportsSportsmen as
SELECT 
    sport_name, 
    COUNT(sportsman.sportsman_id) AS sportsman_quantity
FROM sportsman 
JOIN sportsman_sport
ON sportsman.sportsman_id=sportsman_sport.sportsman_id
GROUP BY sport_name
ORDER BY sportsman_quantity DESC;
'''

query_2 = '''
create view MedalsSportsmen as
SELECT 
    medal, 
    COUNT(medal) AS medals_quantity
FROM sportsman_games
JOIN sportsman 
ON sportsman_games.sportsman_id = sportsman.sportsman_id 
GROUP BY medal
ORDER BY medals_quantity DESC;
'''

query_3 = '''
create view GamesSportsmen as
SELECT 
    games_name,
    COUNT(distinct(sportsman.sportsman_id)) as sportsman_quantity
FROM sportsman
JOIN sportsman_games 
ON sportsman.sportsman_id = sportsman_games.sportsman_id 
GROUP BY games_name
ORDER BY sportsman_quantity DESC;
'''

with con:

    cur2 = con.cursor()
    cur2.execute('DROP VIEW IF EXISTS SportsSportsmen')
    cur2.execute(query_1)
    cur2.execute('SELECT * FROM SportsSportsmen')
    sport_names = []
    sportsmen1 = []

    for row in cur2:
        sport_names.append(row[0])
        sportsmen1.append(row[1])

    cur2 = con.cursor()
    cur2.execute('DROP VIEW IF EXISTS MedalsSportsmen')
    cur2.execute(query_2)
    cur2.execute('SELECT * FROM MedalsSportsmen')
    medals = []
    sportsmen2 = []

    for row in cur2:
        medals.append(row[0])
        sportsmen2.append(row[1])

    cur3 = con.cursor()
    cur3.execute('DROP VIEW IF EXISTS GamesSportsmen')
    cur3.execute(query_3)
    cur3.execute('SELECT * FROM GamesSportsmen')
    games = []
    sportsmen3 = []

    for row in cur3:
        games.append(row[0])
        sportsmen3.append(row[1])


plt.bar(sport_names, sportsmen1, width=0.5, color='green')
plt.xlabel('Sport name')
plt.ylabel('Number of sportsmen')
plt.show()

fig, ax = plt.subplots()
ax.pie(sportsmen2, labels=medals, normalize=True)
plt.axis('equal')
plt.show()

plt.scatter(games, sportsmen3, marker='+', color='red')
plt.show()

