-- Automatically clears existing  DB tournmant, and sets up blank one and
-- connects to it. Avoids icky duplicate data.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament


-- Stores players in tournament.
CREATE TABLE players ( p_id SERIAL primary key,
                       name TEXT );

-- Stores match winners & losers.
CREATE TABLE matches ( m_id SERIAL primary key,
                       winner_id INTEGER references players(p_id),
                       loser_id INTEGER references players(p_id) );

-- View that reports player id, player name, and total wins
CREATE VIEW matches_won AS
    SELECT players.p_id, players.name, COUNT(matches.winner_id) AS wins
    FROM players LEFT JOIN matches on players.p_id = matches.winner_id
    GROUP BY players.p_id
    ORDER BY wins DESC;

-- View that reports player id, player name, and total losses
CREATE VIEW matches_lost AS
    SELECT players.p_id, players.name, COUNT(matches.winner_id) AS losses
    FROM players LEFT JOIN matches on players.p_id = matches.loser_id
    GROUP BY players.p_id
    ORDER BY losses;

-- View that reports player standings (p_id, name, wins, matches played) for
-- each player
CREATE VIEW standings AS
    SELECT matches_won.p_id, matches_won.name, matches_won.wins, COALESCE(matches_won.wins,0) + COALESCE(matches_lost.losses,0) AS matches_played
    FROM matches_won JOIN matches_lost on matches_won.p_id = matches_lost.p_id
    ORDER BY matches_won.wins DESC;

