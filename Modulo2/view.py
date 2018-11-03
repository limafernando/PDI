import numpy as np
import scipy.io.wavfile
from scipy import fftpack
import pydub
from pydub.playback import play
import matplotlib.pyplot as plt
from PIL import Image

def plota(data):
	#Plota o gráfico
	plt.figure('AudioData')
	plt.plot(data, linewidth=0.1, alpha=1,color='blue')
	plt.ylabel('Amplitude')
	plt.show()

def plotaDCTs(dct, dctFiltrada):
	#Plota o gráfico
	plt.figure('Domínio da Frequência')
	plt.subplot(211)
	plt.plot(dct, linewidth=0.1, alpha=1.0, color='blue')
	plt.ylabel('Frequencia')
	plt.subplot(212)
	plt.plot(dctFiltrada, linewidth=0.1, alpha=1.0, color='blue')
	plt.ylabel('Frequencia')
	plt.show()

def passaBaixa(dct):

	dctFiltrada = dct.copy()
	
	for i in range(0, len(dctFiltrada)):
		if abs(dctFiltrada[i]) < 12520:
			dctFiltrada[i] = 0
	
	return dctFiltrada
	
def questao1(n):

	#Lê o arquivo wav: rate é a taxa de amostragem do áudio e audioData são os dados do áudio
	rate, audioData = scipy.io.wavfile.read("audio.wav")

	dct = fftpack.dct(audioData, norm = 'ortho') #Calcula a dct dos dados do áudio
	
	#plota(audioData)

	print(type(audioData[0]))
	
	dctFiltrada = dct.copy()
	
	listadct = dctFiltrada.tolist() 
	indicesMax = []
	
	for i in range(0, len(listadct)):
		listadct[i] = abs(listadct[i])
		
	aux = listadct.copy()
	
	for i in range(0,n):
		indicesMax.append(listadct.index(max(aux)))
		indiceAux = aux.index(max(aux))
		aux.pop(indiceAux)
	
	dctFiltrada = dct.copy()
	
	for i in range(0, len(dctFiltrada)):
		if i not in indicesMax:
			dctFiltrada[i] = 0
	
	dctFiltrada = np.asarray(dctFiltrada)

	
	novoAudio = fftpack.idct(dctFiltrada, norm = 'ortho')
	
	novoAudio = novoAudio.astype("int16")

	print(type(novoAudio[0]))
	
	scipy.io.wavfile.write("audio1.wav", rate, novoAudio)

	#plota(novoAudio)
	
	plotaDCTs(dct, dctFiltrada)
	
def questao2(n):

	imagem = Image.open("lena.bmp")
	imagem.show()
	imagem = np.asarray(imagem)
	
	#print(type(imagem[0][0]))
	
	rc = len(imagem)*len(imagem[0]) #linha coluna
	
	print("RC: ", rc)	
	
	dct = fftpack.dct(fftpack.dct(imagem.T, norm = 'ortho').T, norm = 'ortho') #Calcula a dct dos dados do áudio
	
	
	im = Image.fromarray(dct)
	
	im.show()
	
	listadct = dct.copy()

	list(listadct)
	
	listadct = listadct.tolist()
	
	aux = listadct.copy()
	indices = []
	
	for i in range(0,n):
		
		maior = max([valor for linha in aux for valor in linha])
		
		x = [x for x in aux if maior in x][0]
		
		linha = listadct.index(x)
		coluna = x.index(maior)
	
		aux[linha][coluna] = -1
		
		indices.append(str(linha)+','+str(coluna))
	
	listadct = dct.copy()
	
	for i in range(0, len(imagem)):
		for j in range(0, len(imagem[0])):
			indice = (str(i)+','+str(j))
			if indice not in indices:
				listadct[i][j] = 0
				
	dctFiltrada = np.asarray(listadct)	
	
	im = Image.fromarray(dctFiltrada)
	im.show()
	
	idct = fftpack.idct(fftpack.idct(dctFiltrada.T, norm = 'ortho').T, norm = 'ortho')
	
	#idct = idct.astype("uint8")
	
	#print(type(idct[0][0]))
	
	im = Image.fromarray(idct)
	
	im.show()
	
	
def questao3(c):

	#Lê o arquivo wav: rate é a taxa de amostragem do áudio e audioData são os dados do áudio
	rate, audioData = scipy.io.wavfile.read("audio.wav")

	dct = fftpack.dct(audioData, norm = 'ortho') #Calcula a dct dos dados do áudio

	dctFiltrada = dct.tolist()
	
	if c > 0:
		manter = len(dctFiltrada) - c
		
		lista1 = dctFiltrada[0:manter]
		
		lista2 = [0]*c
		
		dctFiltrada = lista2+lista1
	
	elif(c < 0):
		
		lista1 = dctFiltrada[abs(c):]
		lista2 = [0]*abs(c)
		
		dctFiltrada = lista1+lista2
		
	else:
		pass
		
	dctFiltrada = np.asarray(dctFiltrada)

	novoAudio = fftpack.idct(dctFiltrada, norm = 'ortho')
	
	novoAudio = novoAudio.astype("int16")
	
	scipy.io.wavfile.write("audio3.wav", rate, novoAudio)

	plotaDCTs(dct, dctFiltrada)
	
def main():
	
	print('\n\n1-Questão 1\n' 
		'2-Questão 2\n'
		'3-Questão 3\n')
	op = int(input('Escolha a opção: '))

	if op == 1:
		n = int(input('\nIndique o número de frequências desejadas: '))
		questao1(n)

	elif op == 2:
		n = int(input('\nIndique o número de frequências desejadas: '))
		questao2(n)

	elif op == 3:
		c = int(input('\nIndique o deslocamento desejado: '))
		questao3(c)
	else:
		print('\nTchau')


if __name__ == '__main__':
	main()


'''
	print("Rate: ", rate)
	print("Dados do audio: ", audioData)
	print("Tamanho: ", len(audioData))
	
	#dctFiltrada = passaBaixa(dct)
	
	novoAudio = fftpack.idct(dctFiltrada, norm = 'ortho')
	
	scipy.io.wavfile.write("audio1.wav", rate, novoAudio)
	
	#Lê o arquivo wav
	#wav = pydub.AudioSegment.from_wav("audio.wav")
	
	#Toca a música
	#play(wav)
'''