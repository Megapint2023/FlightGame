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