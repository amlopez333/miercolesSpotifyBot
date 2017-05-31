import requests
import os
import pprint
import sys

import spotipy
import spotipy.util as util

# Credenciales de Spotify deben estar guardados como variables ambiente

#SPOTIPY_CLIENT_ID
#SPOTIPY_CLIENT_SECRET
#SPOTIPY_REDIRECT_URI

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot388739866:AAHgcrhZ-krBh9RbSHcrcOnkh6dELQG1KVo/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        return last_update

#################################################
# greeting_bot =? miercoles_bot
miercoles_bot = BotHandler("bot388739866:AAHgcrhZ-krBh9RbSHcrcOnkh6dELQG1KVo")
#greetings = ('hello', 'hi', 'greetings', 'sup')
#now = datetime.datetime.now()

def main():

    print("Ejecutando...")
    new_offset = None

    # Este while se ejecuta para que el bot esté infinitamente buscando updates de los mensajes recibidos
    # y los muestre en
    # Inicializa el last_message_id en -1
    last_message_id = -1
    # Siempre chequea que el last_message_id sea diferente para que no responda al mismo mensaje dos veces
    while True:

        print("-----------------------------------------------")
        # Guarda el id del mensaje viejo

        old_message_id = last_message_id

        # Consigue un update nuevo

        miercoles_bot.get_updates(new_offset)
        last_update = miercoles_bot.get_last_update()

        # Se guardan variables que están dentro del last_update

        last_update_id = last_update['update_id']
        last_chat_id = last_update['message']['chat']['id']
        last_message_id = last_update['message']['message_id']

        print("Message ID: " + str(last_message_id))
        print("Last update ID: " + str(last_update_id))
        print("Last chat ID: " + str(last_chat_id))

        # Si el último mensaje leído es nuevo, ejecutar

        if(last_message_id != old_message_id):

            # Si el mensaje es de texto

            if 'text' in last_update['message']:
                print("El mensaje es de texto")
                last_chat_text = last_update['message']['text']
                print("Texto: " + last_chat_text)

            # Si el mensaje es foto

            if 'photo' in last_update['message']:
                print("El mensaje es de foto")

            # Personas
            #last_chat_name = last_update['message']['chat']['first_name']
            # Grupos (?)

            last_chat_name = last_update['message']['chat']
            print("Last chat name: " + str(last_chat_name))

            # Si el mensaje contiene una entidad, asumimos que siempre que contenga una, contiene un url, por ahora

            if 'entities' in last_update['message']:

                # Prueba el link si es de spotify con una regex
                print("El ultimo mensaje contiene los URL's: ")
                import re
                urls = re.findall('http[s]?://open.spotify.com/track/[a-zA-Z0-9]+', last_chat_text)
                #idTrack = re.findall('http[s]?://open.spotify.com/track/[a-zA-Z0-9]+', last_chat_text)
                #print("Links: ")
                print(urls)
                # Extrae el Id del track
                username = "edsv5"
                playlist_id = "0lUYvP09zk3XXOZgqkAuof"
                track_id = re.search('http[s]?://open.spotify.com/track/([a-zA-Z0-9]+)', last_chat_text).group(1)
                print("username: " + username + " playlist_id: " + playlist_id + " track_id: " + track_id)

                miercoles_bot.send_message(last_chat_id, "Track ID: " + track_id)
                miercoles_bot.send_message(last_chat_id, "Playlist ID: " + playlist_id)
                ###############################################################

                # Agrega a la playlist (Esta es la parte que no funciona)

                # scope = 'playlist-modify-public'
                # token = util.prompt_for_user_token(username, scope)
                #
                # if token:
                #     sp = spotipy.Spotify(auth=token)
                #     sp.trace = False
                #     results = sp.user_playlist_add_tracks(username, playlist_id, track_id)
                #     print("Agregada track " + track_id + "a playlist")
                #     print (results)
                # else:
                #     print ("Can't get token for", username)

                ###############################################################

                #comando = "spotiPrueba3.py " + username + " " + playlist_id + " " + track_id
                #print("Ejecutando " + comando)
                #os.system(comando)
                #print("Agregada track " + track_id + "a playlist")

                # Agregar el track nuevo al playlist

            #print([last_update, last_update_id, last_chat_text, last_chat_id, last_chat_name])
            #print("Chat: " + str(last_chat_id))
            #print("Ultimo mensaje: " + last_chat_text)
            #print (last_update)
            #print([last_update_id, last_update_id, last_chat_id])



            #miercoles_bot.send_message(last_chat_id, "EJJEJJJJE")
        else:
            print("Esperando mensajes nuevos...")
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
