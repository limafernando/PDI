import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np

import moduloProcessamento as mp

def main():
	print('Escolha a imagem!')
	
	#<Para selecionar o arquivo por GUI
	Tk().withdraw()
	caminhoArquivoOriginal = askopenfilename()
	#caminhoArquivo=os.path.basename(caminhoArquivo) #pega só o nome, mas é importante pegar o caminho
	#Para selecionar o arquivo por GUI>

	imagemOriginal = mp.leImagem(caminhoArquivoOriginal)
	mp.exibeImagem(imagemOriginal)
	arrayImagemOriginal = mp.imagemToArray(imagemOriginal)
	
	altura = len(arrayImagemOriginal)
	largura = len(arrayImagemOriginal[0])

	imagemModificada = None
	arrayImagemModificada = None

	run = True

	while run:
		print('\t\t\t\tMenu\n')
		print('1 - Converter para YIQ')
		print('2 - Converter para RGB')
		print('3 - Imagem com banda individual colorida')
		print('4 - Imagem com banda individual monocromática')
		print('5 - Imagem nagativa')
		print('6 - Controle de brilho aditivo')
		print('7 - Controle de brilho multiplicativo')
		print('8 - Convolução mxn')
		print('9 - Filtro mediana')
		print('10 - Limiarização')
		print('11 - Salvar a imagem modificada')
		print('12 - Encerrar programa')

		opcao = int(input('Escolha a opção: '))

		if opcao == 1:
			arrayImagemModificada = arrayImagemOriginal.copy()
			'''pixel = arrayImagemModificada[0][0]
			pixel[0] = 100
			pixel[1] = 0
			pixel[2] = 0
			print(pixel)'''

			arrayImagemModificada = mp.RGBtoYIQ(arrayImagemModificada, largura, altura)
			'''pixel = arrayImagemModificada[0][0]
			print(pixel)'''
			imagemModificada = mp.arrayToImagem(arrayImagemModificada)
			mp.exibeImagem(imagemModificada)

		elif opcao == 2:
			pixel = arrayImagemModificada[0][0]
			#print(pixel)

			arrayImagemModificada = mp.YIQtoRGB(arrayImagemModificada, largura, altura)

			#pixel = arrayImagemModificada[0][0]
			#print(pixel)

			imagemModificada = mp.arrayToImagem(arrayImagemModificada)
			mp.exibeImagem(imagemModificada)
		
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
		
		elif opcao == 5:
			arrayImagemModificada = mp.negativo(arrayImagemOriginal, largura, altura)
			imagemModificada = mp.arrayToImagem(arrayImagemModificada)
			mp.exibeImagem(imagemModificada)

		elif opcao == 6:
			fator = int(input('Qual o fator de adição? '))
			arrayImagemModificada = mp.controleDeBrilhoAditivo(arrayImagemOriginal, largura, altura, fator)
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
			arrayImagemModificada = mp.limiarizacao(arrayImagemOriginal, largura, altura, m, n)
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




if __name__ == '__main__':
	main()