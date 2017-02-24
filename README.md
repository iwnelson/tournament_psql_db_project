# **Project Title:**
Udacity FSND Project: Tournament Resulsts

# **Project Description**
Includes python file (tournament.py) that contains necessary functions to run a Swiss Pairing System Tournament. These functions will only work properly in a tournament bracket with an even number of players. If an uneven number of players is used - the function swissPairings will no longer work properly.

# **Submodules & Libraries Used:**
    * tournament.psql
        * Includes PostgreSQL tables used in program: players, matches, scoreboard
    * tournament_test.py
        * Python program to test functionality of project functions

# To Run
Using a machine with PostgreSQL and the psql command line interface: follow the following steps:
    * Change directory to project files --> (_ie. cd /tournament_)
    * Create database --> (_ie. CREATE DATABASE tournament_)
    * Connect to database --> (_ie. /c tournament_)
    * Create tables --> (_ie. \i tournament.sql_)
        * Alternatively they can be set up manually via command line - see Supporting Documentation for more information
    * Run tournament_test.py to test functions, or any file of your choosing to put these functions to work!


# Licensing
This content is open source.

# Supporting Documentation
**PostgreSQL Documentation** *https://www.postgresql.org/docs/*
**Python Standard Library** *https://docs.python.org/2.7/library/index.html*

# **Author**
Ian Nelson - ianwalshnelson@gmail.com

Please reach out with any questions or comments. Thanks!
