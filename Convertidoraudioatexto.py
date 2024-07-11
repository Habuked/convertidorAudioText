import speech_recognition as sr
from pydub import AudioSegment

# Convertir el archivo .ogg a .wav
audio = AudioSegment.from_ogg("audio#3.ogg")
audio.export("audio.wav", format="wav")

# Inicializar el reconocedor
recognizer = sr.Recognizer()

# Ruta al archivo de audio convertido
audio_file_path = "audio.wav"

# Transcribir el archivo de audio a texto
with sr.AudioFile(audio_file_path) as source:
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language='es-ES')
        print("Transcripción: " + text)
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError:
        print("Error en el servicio de reconocimiento de voz.")
