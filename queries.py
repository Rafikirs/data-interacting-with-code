# pylint: disable=missing-docstring, C0103
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
a = conn.cursor()


def directors_count(db):
    # return the number of directors contained in the database
    # $CHALLENGIFY_BEGIN
    query = """
        SELECT COUNT(*)
        FROM directors
    """
    db.execute(query)
    count = db.fetchone()
    return count[0]
    # $CHALLENGIFY_END



def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = """
        SELECT name
        FROM directors
        ORDER BY name ASC
    """
    db.execute(query)
    list_of_dir = db.fetchall()
    return [name[0] for name in list_of_dir]

# print (directors_list(db))



def love_movies(db):
    query = """
    SELECT title
        FROM movies
        WHERE UPPER(title) LIKE '% LOVE %'
        OR UPPER(title) LIKE 'LOVE %'
        OR UPPER(title) LIKE '% LOVE'
        OR UPPER(title) LIKE 'LOVE'
        OR UPPER(title) LIKE '% LOVE''%'
        OR UPPER(title) LIKE '% LOVE.'
        OR UPPER(title) LIKE 'LOVE,%'
        ORDER BY title
"""
    db.execute(query)
    love_list = db.fetchall()
    return [name[0] for name in love_list]


def directors_named_like_count(db, name):
    query = f"""
    SELECT COUNT(*)
    FROM directors
    WHERE name LIKE "%{name}%"
    """
    db.execute(query)
    list_of_count_dir = db.fetchone()
    return list_of_count_dir[0]
    # return the number of directors which contain a given word in their name

def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = f"""
    SELECT title
    FROM movies
    WHERE minutes > {min_length}
    ORDER BY title
    """
    db.execute(query)
    list_long_movies = db.fetchall()
    return [film[0] for film in list_long_movies]
