import scipy.io.wavfile
import pydub
from pydub.playback import play
import matplotlib.pyplot as plt
import numpy as np


def main():

	#Lê o arquivo mp3
	mp3 = pydub.AudioSegment.from_mp3("UnderPressure.mp3")
	
	#Converte para o formato wav
	mp3.export("UnderPressure.wav", format="wav")
	
	#Lê o arquivo wav: rate é a taxa de amostragem do áudio e audioData são os dados do áudio
	rate, audioData = scipy.io.wavfile.read("UnderPressure.wav")
	
	
	print("Rate: ", rate)
	print("Dados do audio: ", audioData)
	print(audioData.dtype)
	
	"""
	#Manipula os dados do áudio e salva
	scipy.io.wavfile.write("UnderPressure.wav", int(rate*2), audioData)

	#Lê o arquivo wav
	wav = pydub.AudioSegment.from_wav("UnderPressure.wav")
	
	#Toca a música
	play(wav)
	"""
	
	#Calcula uma variável tempo para utilizar no gráfico
	tempo = np.arange(0, float(audioData.shape[0]), 1) / rate

	#Plota o gráfico
	plt.figure(1)
	plt.plot(tempo, audioData, linewidth=0.01, alpha=0.7, color='#ff7f00')
	plt.xlabel('Tempo (s)')
	plt.ylabel('Amplitude')
	plt.show()
	
	
	
main()