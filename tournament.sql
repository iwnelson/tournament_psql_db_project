
CREATE TABLE players ( p_id SERIAL primary key,
                       name TEXT );

CREATE TABLE matches ( m_id SERIAL primary key,
                       winner_id INTEGER,
                       loser_id INTEGER );

CREATE TABLE scoreboard ( p_id INTEGER primary key,
                          wins INTEGER,
                          losses INTEGER,
                          matches INTEGER);
