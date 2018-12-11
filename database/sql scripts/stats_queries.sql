-- Query 1: Return all teams in database
USE ncaam_basketball_2017_db;
SELECT t.id AS team_id,
		t.name AS Team_name,        
        t.region_id,
        r.name AS Region,
        mascot
FROM team t
JOIN region r ON(t.region_id = r.id);

-- Query 2 Return all players in database
USE ncaam_basketball_2017_db;
SELECT	pl.id AS player_id,
		pl.name,
        pl.height,
        pl.weight,
        pl.DOB,
        pl.position_id,
        pos.name AS position,
        pl.team_id,
        t.name as Team
FROM players pl
JOIN positions pos ON(pl.position_id = pos.id)
JOIN team t ON(pl.team_id = t.id);

-- Query 3: Return all player stats, stats for all games
USE ncaam_basketball_2017_db;
SELECT * FROM player_stats;

-- Query 4: Return all team stats from all games
USE ncaam_basketball_2017_db;
SELECT * FROM team_stats;

