#LISTA - TIETOKANTAKYSELYT

# Kysely: jolla saadaan vihje missä maassa matkalaukku on ICAO:n avulla
def query_country_hint(case_location):
    sql_query_country_hint = (f"SELECT hint, name FROM country WHERE iso_country in ("
                              f"SELECT iso_country FROM airport WHERE ident = '{case_location}');")
    return sql_query_country_hint

# Kysely: palauttaa maat aakkosjärjestyksessä
query_countries = f"SELECT name FROM country WHERE continent = 'EU' ORDER BY name;"

# Kysely: saadaan parametri country avulla kyseisen maan lentokenttien ICAOT järjestyksessä large tyypistä alaspäin
def query_country_airports(country):
    sql_query_airports = (f"SELECT ident FROM airport, country "
                          f"WHERE airport.iso_country = country.iso_country and country.name ='{country}'"
                          f"ORDER BY CASE WHEN type = 'large_airport' THEN 1 WHEN type = 'medium_airport' THEN 2 WHEN type = 'small_airport' THEN 3 ELSE 4 END")
    return sql_query_airports

# Kysely: jolla saadaan etäisyys pelaajan ja jonkun toisen paikan välillä, (float metreissä)
def query_distance_between_player_locations(playername, icao2):
    sql_query_distance = (f"SELECT ST_Distance_Sphere("
                          f"ST_GeomFromText(("
                          f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident in (SELECT location FROM game WHERE id = '{playername}')), 4326), "
                          f"ST_GeomFromText(("
                          f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident = '{icao2}', 4326));")
    return sql_query_distance

# Kysely: jolla saadaan etäisyys kahden paikan väliltä metreissä float
def query_distance_between_locations(icao1, icao2):
    sql_query_distance = (f"SELECT ST_Distance_Sphere("
                          f"ST_GeomFromText(("
                          f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident = '{icao1}'), 4326, "
                          f"ST_GeomFromText(("
                          f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident = '{icao2}', 4326));")
    return sql_query_distance

# LOAD
# Kysely: Pelaajan tiedot / status
def query_load_username(username):
    sql_query_load_username = (f"SELECT game.id, game.location, suitcase.location, co2_consumed. total_kilometers, clue_unlocked, travel_count "
                               f"FROM game, suitcase WHERE game.id = suitcase.id and game.id ='{username}';")
    return sql_query_load_username
# Kysely jolla päivitetään uusi käyttäjä myös suitcase tauluun
def query_new_suitcase(username):
    sql_query_new_suitcase = (f"INSERT INTO suitcase (id) VALUES ('{username}');")
    return sql_query_new_suitcase
# Kysely: tallennedtaan uusin pelaaja tietokantaan ja asetetaan alkuarvot
def query_new_username(username):
    sql_query_new_username = (f" INSERT INTO game (id, location, co2_consumed, total_kilometers, clue_unlocked, travel_count, suitcase_found) VALUES ('{username}', 'EFHK', 0, 0, 0, 0, 0,);")
    return sql_query_new_username
# Tarkistaa onko kyseinen pelaaja jo tietokannasta
def query_check_username(username):
    sql_query_check_username = (f"SELECT id FROM game WHERE id = '{username}';")
    return sql_query_check_username
# Kysely jolla saadaan käyttäjän maa LOWER-casena
def query_fetch_user_country(username):
    sql_query_fetch_user_country = (f"SELECT LOWER(name) FROM country WHERE iso_country in("
                                    f"SELECT iso_country FROM airport WHERE ident in("
                                    f"SELECT location FROM game WHERE id = '{username}'));")
    return sql_query_fetch_user_country
# Kysely jolla saadaan käyttäjän matkalaukun maa LOWER - casena
def query_fetch_suitcase_country(username):
    sql_query_fetch_suitcase_country = (f"SELECT LOWER(name) FROM country WHERE iso_country in("
                                        f"SELECT iso_country FROM airport WHERE ident in("
                                        f"SELECT location FROM suitcase WHERE id = '{username}'));")
    return sql_query_fetch_suitcase_country
# Kysely jolla haetaan tietokannasta ihmiset joilla on vähintään yli 1 matkalaukku ja max 5 ihmistä dest order
sql_query_fetch_leaderboards = (f"SELECT id, suitcase_found FROM game WHERE suitcase_found >= 1 order by suitcase_found desc LIMIT 5;")
# Vakio jolla saadaan olemassaolevat käyttäjät
sql_query_fetch_users = (f"SELECT id FROM game")

# UPDATE

def query_update_suitcase_location(location, username):
    sql_query_update_suitcase_location = (f"UPDATE suitcase SET location = ('{location}') WHERE id = '{username}';")
    return sql_query_update_suitcase_location
# Lisätään pelaajalle kilometrit, co2 määrä, travel count, location tietokantaan talteen
def query_update_player_travel(username, kilometers, count, location):
    sql_query_update_player_travel =  (f"UPDATE game SET location = '{location}', total_kilometers = {kilometers}+total_kilometers, so2_consumed = {kilometers*8}+co2_consumed, travel_count = {count}+travel_count WHERE id = '{username}';")
    return sql_query_update_player_travel
# Päivittää ja ilmoittaa jos pelaaja avaa vihjeen
def query_update_clue_unlocked(username, int):
    sql_query_update_player_travel = (f"UPDATE game SET clue_unlocked = {int} WHERE id = '{username}';")
    return sql_query_update_player_travel
# Päivittää pelin takaisin alkuun ja lisätään pelaajalle 1 matkalaukku löydetty
def query_reset_game_state(username):
    sql_query_reset_game_state = (f"UPDATE game SET location = 'EFHK' , clue_unlocked = 0, total_kilometers = 0, co2_consumed = 0, travel_count = 0, suitcases_found+1 WHERE id = '{username}';")
    return sql_query_reset_game_state
