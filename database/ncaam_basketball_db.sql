DROP DATABASE IF EXISTS ncaam_basketball_db;

CREATE DATABASE ncaam_basketball_db;

USE ncaam_basketball_db;


DROP TABLE IF EXISTS region;

CREATE TABLE region(
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(50)

);

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
region_id INT,

INDEX (region_id),

foreign key (region_id)
REFERENCES region(id)
ON UPDATE CASCADE ON DELETE RESTRICT,
name VARCHAR(50)

);

DROP TABLE IF EXISTS game;
CREATE TABLE game(
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
tournament_round_id INT NOT NULL,
region_id INT,
team_play VARCHAR(100),
winner VARCHAR(100),
loser VARCHAR(100),
score INT,


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
OREB INT,
REB INT,
AST INT,
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
OREB INT,
REB INT,
AST INT,
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

USE ncaam_basketball_db;

INSERT INTO region(name)
	VALUES
    ('south'),
    ('east'),
    ('west'),
    ('midwest');

SELECT * FROM region;


INSERT INTO tournament_round(name, region_id)
	VALUES
    ('first round', 1),
    ('first round', 2),
    ('first round', 3),
    ('first round', 4),
    ('second round', 1),
    ('second round', 2),
    ('second round', 3),
    ('second round', 4),
    ('regional semifinals', 1),
    ('regional semifinals', 2),
    ('regional semifinals', 3),
    ('regional semifinals', 4),
    ('regional finals', 1),
    ('regional finals', 2),
    ('regional finals', 3),
    ('regional finals', 4);
    
    
SELECT * FROM tournament_round;


INSERT INTO tournament_round(name)
	VALUES
    
    ('final four A'),
    ('final four B'),
    ('national championship');


SELECT * FROM tournament_round;


INSERT INTO positions(name, abrv)
	VALUES
    ('gaurd','G'),
    ('forward','F'),
    ('center', 'C');
    
    
SELECT * FROM positions;

SELECT * FROM region;

INSERT INTO team(name, region_id)
	VALUES
    
	('Virginia', 1),
    ('UMBC',1),
    ('Creighton',1),
    ('Kansas St.',1),
    ('Kentucky', 1),
    ('Davidson', 1),
    ('Arizona', 1),
    ('Buffalo',1),
    ('Miami (Fla.)',1),
    ('Loyola Chicago',1),
    ('Tennessee',1),
    ('Wright St.',1),
    ('Nevada',1),
    ('Texas',1),
    ('Cincinnati',1),
    ('Georgia St.',1),
    ('Villanova',2),
    ('Radford',2),
    ('Virginia Tech',2),
    ('Alabama',2),
    ('West Virginia',2),
    ('Murray St.',2),
    ('Wichita St.',2),
    ('Marshall',2),
    ('Florida',2),
    ('St. Bonaventure',2),
    ('Texas Tech',2),
    ('S.F. Austin',2),
    ('Arkansas',2),
    ('Butler',2),
    ('Purdue',2),
    ('CSU Fullerton',2),
    ('Kansas',4),
    ('Penn',4),
    ('Seton Hall',4),
    ('NC St.',4),
    ('Clemson',4),
    ('New Mexico St.',4),
    ('Auburn',4),
    ('Charleston',4),
    ('TCU',4),
    ('Syracuse',4),
    ('Michigan St.',4),
    ('Bucknell',4),
    ('Rhode Island',4),
    ('Oklahoma',4),
    ('Duke',4),
    ('Iona',4),
    ('Xavier',3),
    ('Texas Southern',3),
    ('Missouri',3),
    ('Florida St.',3),
    ('Ohio St',3),
    ('S. Dakota St.',3),
    ('Gonzaga ',3),
    ('UNCG',3),
    ('Houston',3),
    ('San Diego St.',3),
    ('Michigan',3),
    ('Montana',3),
    ('Texas A&M',3),
    ('Providence',3),
    ('North Carolina',3),
    ('Lipscomb',3);
    
    
SELECT t.name, 
	   r.name,
       r.id
FROM team t

JOIN region r

ON (t.region_id = r.id)

WHERE t.region_id = 1;

    
    
    
    
    
    
    
    