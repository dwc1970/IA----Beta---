import speech_recognition as sr
import pyttsx3


def speak(text) :
    engine = pyttsx3.init ( )
    engine.say ( text )
    engine.runAndWait ( )


def listen() :
    recognizer = sr.Recognizer ( )

    with sr.Microphone ( ) as source :
        print ( "Escuchando..." )
        recognizer.pause_threshold = 1
        audio = recognizer.listen ( source )

    try :
        print ( "Reconociendo..." )
        query = recognizer.recognize_google ( audio , language="es-ES" )
        print ( f"Tú: {query}" )
        return query.lower ( )
    except Exception as e :
        print ( e )
        return None


def get_response(query) :
    responses = {
        "hola" : "¡Hola! ¿Cómo estás?" ,
        "bien" : "Me alegra escuchar que estás bien." ,
        "¿cuál es tu nombre?" : "Soy un asistente de voz creado en Python." ,
        "¿cuál es el clima hoy?" : "Lo siento, no puedo proporcionar información sobre el clima en este momento." ,
        "adiós" : "Hasta luego. ¡Que tengas un buen día!"
    }

    response = responses.get ( query , "Lo siento, no puedo responder a eso." )
    return response


def assistant() :

    speak ( "vamos a la playa andres ?" )

    while True :
        query = listen ( )
        if query :
            response = get_response ( query )
            speak ( response )
            if "adiós" in query :
                break


if __name__ == "__main__" :
    assistant ( )
