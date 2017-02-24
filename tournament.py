#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches")
    c.execute("UPDATE scoreboard SET wins = 0, losses = 0, matches = 0")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players")
    c.execute("DELETE FROM scoreboard")
    c.execute("DELETE FROM matches")
    DB.commit()
    DB.close()



def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT COUNT(*) AS num FROM PLAYERS")
    count = int(c.fetchone()[0])
    DB.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s) RETURNING p_id", (name,))
    p_id = c.fetchone()[0]
    c.execute("""INSERT INTO scoreboard (p_id, wins, losses, matches) VALUES
                 (%s, 0, 0, 0)""", (p_id,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute("""SELECT players.p_id, players.name, scoreboard.wins,
                 scoreboard.matches FROM players, scoreboard WHERE
                 players.p_id = scoreboard.p_id ORDER BY wins DESC""")
    standings = [[row[0], row[1], row[2], row[3]] for row in c.fetchall()]
    DB.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    c.execute("""INSERT INTO matches (winner_id, loser_id) VALUES
                 (%s, %s)""", (winner, loser,))
    c.execute("""UPDATE scoreboard SET wins = wins+1, matches = matches+1 WHERE
                 p_id = %s""", (winner,))
    c.execute("""UPDATE scoreboard SET losses = losses+1, matches = matches+1 WHERE
                 p_id = %s""", (loser,))
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    pairs = []
    if len(standings) % 2 == 0:
        while len(standings) > 0:
            p2 = standings.pop()
            p1 = standings.pop()
            pairs.append([p1[0], p1[1], p2[0], p2[1]])
    return pairs
