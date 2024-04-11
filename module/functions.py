#Se obtiene el diccionario del jugador con mas goles realizados
def best_player(statistics):
    player_max_goals = max(statistics, key = lambda player: player["Goles"])
    return player_max_goals

#Se muestran los datos del goleador
def info_best_player(statistics):
    info =  best_player(statistics)
    return (f'El goleador del partido es {info["Nombre"]} con {info["Goles"]} goles')



# Calculamos los puntos de cada jugador
def points(player):
    return player["Goles"]*1.5 + player["Goles evitados"]*1.5 + player["Asistencias"]

#Se obtiene el diccionario cuyo jugador tiene mayor puntaje
def influential_player(statistics):
        player = max(statistics, key=points)
        return (f'El jugador mas influyente fue {player["Nombre"]} con un total de {points(player)} puntos')





