# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id SERIAL PRIMARY KEY, start_time BIGINT NOT NULL, user_id INT NOT NULL, level VARCHAR , 
                                                        song_id VARCHAR, artist_id VARCHAR, session_id VARCHAR, location VARCHAR, user_agent VARCHAR)
""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS users (user_id INT PRIMARY KEY, first_name VARCHAR, last_name VARCHAR, gender VARCHAR, level VARCHAR)
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs(table_id SERIAL PRIMARY KEY, song_id VARCHAR, title VARCHAR, artist_id VARCHAR NOT NULL, year INT, duration FLOAT)
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists(table_id SERIAL PRIMARY KEY, artist_id VARCHAR, artist_name VARCHAR, location VARCHAR, latitude FLOAT, longitude FLOAT)
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (table_id SERIAL PRIMARY KEY, start_time BIGINT, hour INT, day INT, week INT, month INT, year INT, weekday INT)
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays(start_time, user_id, level, song_id, artist_id , session_id , location, user_agent)
                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level)
                        VALUES (%s,%s,%s,%s,%s)
                        ON CONFLICT (user_id)
                        DO UPDATE SET LEVEL = EXCLUDED.LEVEL
""")

song_table_insert = (""" INSERT INTO  songs(song_id, title, artist_id, year, duration)
                        VALUES (%s,%s,%s,%s,%s)
                        ON CONFLICT (table_id)
                        DO NOTHING
""")

artist_table_insert = (""" INSERT INTO artists(artist_id, artist_name, location, latitude, longitude)
                            VALUES (%s,%s,%s,%s,%s)
                        ON CONFLICT (table_id)
                        DO NOTHING                            
""")


time_table_insert = (""" INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                         VALUES (%s,%s,%s,%s,%s,%s,%s)
                        ON CONFLICT (table_id)
                        DO NOTHING
""")

# FIND SONGS

song_select = (""" SELECT songs.song_id, artists.artist_id FROM songs
                   JOIN artists ON songs.artist_id = artists.artist_id
                   WHERE songs.title = %s AND artists.artist_name = %s AND songs.duration = %s 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]