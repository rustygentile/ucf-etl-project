DROP DATABASE IF EXISTS ncaam_basketball_2018_db;

CREATE DATABASE ncaam_basketball_2018_db;

USE ncaam_basketball_2018_db;


DROP TABLE IF EXISTS region;

CREATE TABLE region(
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(50)

);

USE ncaam_basketball_2018test_db;

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

rank INT,

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

    ('Elite 8', 1, '2018-03-24'),
    ('Elite 8', 2, '2018-03-25'),
    ('Elite 8', 3, '2018-03-24'),
    ('Elite 8', 4, '2018-03-25');
    

INSERT INTO tournament_round(name, date)
	VALUES
    
    ('final four A', '2018-03-31'),
    ('final four B', '2018-03-31'),
    ('national championship','2018-04-02');




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
    
    
INSERT INTO team(name, region_id, rank)
	VALUES
    

   
    ('Kansas',4,1),           -- elite 8
    ('Duke', 4,2),        -- elite 8
    
    ('Michigan',3,3),  -- elite 8
    ('Florida St',3, 9), -- elite 8
    
   
    ('Kansas St.',1, 9),       -- elite 8
    ('Loyola',1, 11), -- elite 8
 

    ('Villanova',2, 1),  -- elite 8
     ('Texas Tech',2,3);       -- elite 8
    






