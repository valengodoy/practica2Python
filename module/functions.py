#Se obtiene el diccionario del jugador con mas goles realizados
def best_player(statistics):
    player_max_goals = max(statistics, key = lambda player: player["Goles"])
    return player_max_goals

#Se muestran los datos del goleador
def info_best_player(statistics):
    info =  best_player(statistics)
    return (f'El goleador del partido es {info["Nombre"]} con {info["Goles"]} goles')




