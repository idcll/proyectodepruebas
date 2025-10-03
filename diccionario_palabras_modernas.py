import time
print("Diccionario de palabras modernas")
time.sleep(3)

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "LORE": "Contexto, Historia o Transfondo de algo",
            "HYPE": "Emocion o expectativa alta",
            "EZ": "Muy facil",
            "GG":"Buena partida",
            "DELULU": "Iluso",
            "FLEXEAR": "Presumir",
            "WP": "Well Played (Bien jugado, en inglés)",
            "OP": "Overpowered, se usa para un objeto, item o función en videojuegos que tenga bastante poder.",
            "SLAY": "Algo que es espectacular o increíble. ",
            "BRO": "Hermano, amigo, compañero",
            "OMG": "Oh por dios (traducción literal del inglés)",
            "NO WAY": "No hay forma / De ninguna manera"
            }
word = input("Escribe una palabra que no entiendas (¡Con mayúsculas)")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Palabra no encontrada")
    
