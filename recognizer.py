#Código que escuta um comando de soma em inglês e retorna a resposta em áudio.
#Teste dizer: five plus two
#A resposta correta deve ser: 7 (sete)

import speech_recognition
import pyttsx3

#Inicializa o objeto que reconhece o áudio
recognizer = speech_recognition.Recognizer()
#Com o acesso ao microfone, a variável "audio" capta a entrada de som do microfone.
with speech_recognition.Microphone() as entrada:
    print("say something: ")
    audio = recognizer.listen(entrada)

#Separa o que foi "escutado" em uma lista.
palavras = recognizer.recognize_google(audio).split()

#Faz a soma dos valores que estão na posição 0 e 2 da lista. A posição 1 é o plus.
conta=int(palavras[0])+int(palavras[2])
print(conta)

#Diz o número somado.
engine = pyttsx3.init()
engine.say(str(conta))
engine.runAndWait()

