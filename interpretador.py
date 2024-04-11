import speech_recognition as sr
from deep_translator import GoogleTranslator
import pyttsx3

def trans(text, target_language='en'):
    translator = GoogleTranslator(source='auto', target=target_language)
    translated_text = translator.translate(text)
    print(translated_text)
    engine.say(translated_text)
    engine.runAndWait()

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Configurar a voz masculina (se disponível)
voices = engine.getProperty('voices')
for voice in voices:
    if "male" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

with sr.Microphone() as source:
    print("Limpando sons de fundo")
    recognizer.adjust_for_ambient_noise(source)
    print("Esperando mensagem")
    audio = recognizer.listen(source)
    print("Terminando de gravar")

try:
    print('Gravando')
    result = recognizer.recognize_google(audio, language='pt')
    print('Texto Reconhecido:', result)
    trans(result, target_language='en')  # Altere  para o código do idioma desejado
except sr.UnknownValueError:
    print("Não entendi a fala")
except sr.RequestError as ex:
    print("Erro ao solicitar reconhecimento de fala; {0}".format(ex))
except Exception as ex:
    print("Erro inesperado: {0}".format(ex))
