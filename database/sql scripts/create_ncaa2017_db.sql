DROP DATABASE IF EXISTS ncaam_basketball_2017_db;

CREATE DATABASE ncaam_basketball_2017_db;

USE ncaam_basketball_2017_db;


DROP TABLE IF EXISTS region;

CREATE TABLE region(
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(50)

);

USE ncaam_basketball_2017_db;

INSERT INTO region(name)
	VALUES
    ('south'),
    ('east'),
    ('west'),
    ('midwest');


DROP TABLE IF EXISTS team;

CREATE TABLE team(
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(50),
region_id INT NOT NULL,

INDEX (region_id),

foreign key (region_id)
REFERENCES region(id)
ON UPDATE CASCADE ON DELETE RESTRICT,
mascot VARCHAR(50)

);

DROP TABLE IF EXISTS positions;

CREATE TABLE positions(
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(50),
abrv VARCHAR(2)

);


DROP TABLE IF EXISTS tournament_round;

CREATE TABLE tournament_round(
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
date VARCHAR(50),
region_id INT,

INDEX (region_id),

foreign key (region_id)
REFERENCES region(id)
ON UPDATE CASCADE ON DELETE RESTRICT,
name VARCHAR(50)

);


INSERT INTO tournament_round(name, region_id, date)
	VALUES
    ('first four', 1, '2017-03-14'),
    ('first four', 2, '2017-03-14'),
    ('first four', 2, '2017-03-14'),
    ('first four', 4, '2017-03-15'),
    ('first round', 1, '2017-03-16'),
    ('first round', 1, '2017-03-17'),
    ('first round', 2, '2017-03-16'),
    ('first round', 2, '2017-03-17'),
    ('first round', 3, '2017-03-16'),
    ('first round', 4, '2017-03-16'),
    ('first round', 4, '2017-03-17'),
    ('second round', 1, '2017-03-18'),
    ('second round', 1, '2017-03-19'),
    ('second round', 2,'2017-03-18'),
    ('second round', 2,'2017-03-19'),
    ('second round', 3, '2017-03-18'),
    ('second round', 4, '2017-03-18'),
    ('second round', 4, '2017-03-19'),
    ('regional semifinals', 1,'2017-03-24'),
    ('regional semifinals', 2, '2017-03-24'),
    ('regional semifinals', 3, '2017-03-24'),
    ('regional semifinals', 4, '2017-03-23'),
    ('regional finals', 1, '2017-03-26'),
    ('regional finals', 2, '2017-03-26'),
    ('regional finals', 3, '2017-03-25'),
    ('regional finals', 4, '2017-03-25');
    

INSERT INTO tournament_round(name, date)
	VALUES
    
    ('final four A', '2017-04-01'),
    ('final four B', '2017-04-01'),
    ('national championship','2017-04-03');




DROP TABLE IF EXISTS game;
CREATE TABLE game(
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
tournament_round_id INT NOT NULL,
region_id INT,
team_play VARCHAR(100),
winner VARCHAR(100),
loser VARCHAR(100),
score VARCHAR(50),


INDEX(tournament_round_id),
INDEX(region_id),

foreign key (tournament_round_id)
REFERENCES tournament_round(id)
ON UPDATE CASCADE ON DELETE RESTRICT,
foreign key(region_id)
REFERENCES region(id)

);

DROP TABLE IF EXISTS players;

CREATE TABLE players(

id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(100),
height VARCHAR(50),
weight VARCHAR(50),
DOB VARCHAR(50),
position_id INT NOT NULL ,
team_id INT NOT NULL,

INDEX(position_id),
INDEX(team_id),

FOREIGN KEY (position_id)
REFERENCES positions(id)
ON UPDATE CASCADE ON DELETE RESTRICT,
FOREIGN KEY (team_id)
REFERENCES team(id)
ON UPDATE CASCADE ON DELETE RESTRICT

);

DROP TABLE IF EXISTS tournament_dates;


DROP TABLE IF EXISTS player_stats;

CREATE TABLE player_stats(

player_id INT NOT NULL,
game_id INT NOT NULL,

INDEX(player_id),
INDEX(game_id),

FOREIGN KEY (player_id)
REFERENCES players(id)
ON UPDATE CASCADE ON DELETE RESTRICT,
FOREIGN KEY (game_id)
REFERENCES game(id)
ON UPDATE CASCADE ON DELETE RESTRICT,

Min INT,
FGM INT,
FGA INT,
3PA INT,
3PM INT,
FTA INT,
FTM INT,
OREB INT,
REB INT,
AST INT,
ST INT,
BLK INT, 
Turnover INT,
PF INT, 
PTS INT

);

DROP TABLE IF EXISTS team_stats;

CREATE TABLE team_stats(

team_id INT NOT NULL,
game_id INT NOT NULL,
FGM INT,
FGA INT,
3PA INT,
3PM INT,
FTA INT,
FTM INT,
OREB INT,
REB INT,
AST INT,
ST INT,
BLK INT, 
Turnover INT,
PF INT, 
PTS INT,

INDEX (team_id),
INDEX (game_id),

FOREIGN KEY (team_id)
REFERENCES team(id)
ON UPDATE CASCADE ON DELETE RESTRICT,

FOREIGN KEY (game_id)
REFERENCES game(id)
ON UPDATE CASCADE ON DELETE RESTRICT

);


INSERT INTO positions(name, abrv)
	VALUES
    ('gaurd','G'),
    ('forward','F'),
    ('center', 'C');
    
    
INSERT INTO team(name, region_id)
	VALUES
    
	('Wake Forest', 1),
    ('Texas Southern',1),
    ('North Carolina',1),
    ('Kansas St',1),
    ('Arkansas', 1),
    ('Seton Hall', 1),
    ('Minnesota', 1),
    ('Middle Tenn.',1),
    ('Butler',1),
    ('Winthrop',1),
    ('Cincinnati',1),
    ('UCLA',1),
    ('Kent St.',1),
    ('Dayton',1),
    ('Wichita St',1),
    ('Kentucky',1),
    ('Northern Ky.',1),
    ('Mount St. Mary’s',2),
    ('New Orleans',2),
    ('Virginia Tech',2),
    ('Villanova',2),
    ('Wisconsin',2),
    ('Virginia',2),
    ('UNC Wilmington',2),
    ('Florida',2),
    ('East Tenn. St.',2),
    ('SMU',2),
    ('USC',2),
    ('Baylor',2),
    ('New Mexico St.',2),
    ('South Carolina',2),
    ('Marquette',2),
    ('Duke',2),
    ('Troy',2),
    ('Kansas',4),
    ('UC Davis',4),
    ('Miami (Fla.)',4),
    ('Michigan St.',4),
    ('Iowa St.',4),
    ('Nevada',4),
    ('Purdue',4),
    ('Vermont',4),
    ('Creighton',4),
    ('Rhode Island',4),
    ('Oregon',4),
    ('Iona',4),
    ('Michigan',4),
    ('Oklahoma St.',4),
    ('Louisville',4),
    ('Jacksonville St.',4),
    ('N.C. Central',4),
    ('Gonzaga',3),
    ('S.Dakota St',3),
    ('Northwestern',3),
    ('Vanderbilt',3),
    ('Notre Dame',3),
    ('West Virginia',3),
    ('Bucknell ',3),
    ('Maryland',3),
    ('Xavier',3),
    ('Florida St',3),
    ('Fla. Gulf Coast',3),
    ('Arizona',3),
    ('Saint Mary’s',3),
    ('VCU',3),
    ('North Dakota',3);







