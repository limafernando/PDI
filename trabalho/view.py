import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np
from PIL import Image

import moduloProcessamento as mp

def main():
	print('Escolha a imagem!')
	
	#Para selecionar o arquivo por GUI#
	Tk().withdraw()
	caminhoArquivoOriginal = askopenfilename()
	#Para selecionar o arquivo por GUI#

	imagemOriginal = mp.leImagem(caminhoArquivoOriginal)
	mp.exibeImagem(imagemOriginal)
	arrayImagemOriginal = mp.imagemToArray(imagemOriginal)
	
	altura = len(arrayImagemOriginal)
	largura = len(arrayImagemOriginal[0])

	imagemModificada = None
	arrayImagemModificada = None

	run = True
	imagemModificaIsRGB = True

	while run:
		print('\t\t\t\tMenu\n')
		print('1 - Converter para YIQ')
		print('2 - Converter para RGB')
		print('3 - Imagem com banda individual colorida')
		print('4 - Imagem com banda individual monocromática')
		print('5 - Imagem negativa')
		print('6 - Controle de brilho aditivo')
		print('7 - Controle de brilho multiplicativo')
		print('8 - Convolução mxn')
		print('9 - Filtro mediana')
		print('10 - Limiarização')
		print('11 - Salvar a imagem modificada')
		print('12 - Encerrar programa')

		opcao = int(input('Escolha a opção: '))

		if opcao == 1:
			arrayImagemModificada = mp.RGBtoYIQ(arrayImagemOriginal, largura, altura)			
			imagemModificada = mp.arrayToImagem(arrayImagemModificada)
			mp.exibeImagem(imagemModificada)
			imagemModificaIsRGB = False

		elif opcao == 2:
			arrayImagemModificada = mp.YIQtoRGB(arrayImagemModificada, largura, altura)
			imagemModificada = mp.arrayToImagem(arrayImagemModificada)
			mp.exibeImagem(imagemModificada)
			imagemModificaIsRGB = True
		
		elif opcao == 3:
			banda = input('Para qual banda? ')
			arrayImagemModificada = mp.bandaIndividual(arrayImagemOriginal, largura, altura, banda)
			imagemModificada = mp.arrayToImagem(arrayImagemModificada)
			mp.exibeImagem(imagemModificada)
		
		elif opcao == 4:
			banda = input('Para qual banda? ')
			arrayImagemModificada = mp.monocromatica(arrayImagemOriginal, largura, altura, banda)
			imagemModificada = mp.arrayToImagem(arrayImagemModificada)
			mp.exibeImagem(imagemModificada)
		
		elif opcao == 5: #Negativo
			if imagemModificaIsRGB is True:
				arrayImagemModificada = mp.negativoRGB(arrayImagemOriginal, largura, altura)
				imagemModificada = mp.arrayToImagem(arrayImagemModificada)
				mp.exibeImagem(imagemModificada)
			
			else:
				arrayImagemModificada = mp.negativoYIQ(arrayImagemModificada, largura, altura)
				imagemModificada = mp.arrayToImagem(arrayImagemModificada)
				mp.exibeImagem(imagemModificada)

		elif opcao == 6: #BrilhoAditivo
			fator = int(input('Qual o fator de adição? '))

			if imagemModificaIsRGB is True:
				arrayImagemModificada = mp.controleDeBrilhoAditivoRGB(arrayImagemOriginal, largura, altura, fator)
				imagemModificada = mp.arrayToImagem(arrayImagemModificada)
				mp.exibeImagem(imagemModificada)
			
			else:
				arrayImagemModificada = mp.controleDeBrilhoAditivoYIQ(arrayImagemModificada, largura, altura, fator)
				imagemModificada = mp.arrayToImagem(arrayImagemModificada)
				mp.exibeImagem(imagemModificada)
			

		elif opcao == 7:
			fator = float(input('Qual o fator de multiplicação? '))
			arrayImagemModificada = mp.controleDeBrilhoMultiplicativo(arrayImagemOriginal, largura, altura, fator)
			imagemModificada = mp.arrayToImagem(arrayImagemModificada)
			mp.exibeImagem(imagemModificada)

		elif opcao == 8:
			mascara = input('Qual é a máscara? ')
			arrayImagemModificada = mp.convolucao(arrayImagemOriginal, largura, altura, mascara)
			imagemModificada = mp.arrayToImagem(arrayImagemModificada)
			mp.exibeImagem(imagemModificada)

		elif opcao == 9:
			m = int(input('Qual é a qtd de linhas? '))
			m = int(input('Qual é a qtd de colunas? '))
			arrayImagemModificada = mp.filtroMediana(arrayImagemOriginal, largura, altura, m, n)
			imagemModificada = mp.arrayToImagem(arrayImagemModificada)
			mp.exibeImagem(imagemModificada)

		elif opcao == 10:
			limiar = int(input('Qual é o limiar? '))
			banda = input('Para qual banda? ')
			arrayImagemModificada = mp.limiarizacao(arrayImagemOriginal, largura, altura, limiar, banda)
			imagemModificada = mp.arrayToImagem(arrayImagemModificada)
			mp.exibeImagem(imagemModificada)

		elif opcao == 11:
			print('Salvando...')
			mp.salvaImagem(imagemModificada, caminhoArquivoOriginal)

		elif opcao == 12:
			print('Encerrando...')
			run = False
		else:
			print('Opção inválida!')

#############################################################################

if __name__ == '__main__':
	main()