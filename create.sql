create table sportsman(
	sportsman_id int primary key not null,
	sportsman_name varchar(50),
	country varchar(20)
);

create table games(
	games_name varchar(20) primary key not null,
	games_year int,
	games_city varchar(30)
);


create table sportsman_games(
	id int primary key not null,
	sportsman_id int references sportsman(sportsman_id),
	games_name varchar(20) references games(games_name),
	medal varchar(6)
);

create table sport(
	sport_name varchar(20) primary key not null
);

create table sportsman_sport(
	id int primary key not null,
	sport_name varchar(20) references sport(sport_name),
	sportsman_id int references sportsman(sportsman_id)
);