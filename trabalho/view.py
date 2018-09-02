import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np

import moduloProcessamento as mp

def main():
	print('escolha o arquivo')
	
	Tk().withdraw() #we don't want a full GUI, so keep the root window from appearing
	filename = askopenfilename() #show an "Open" dialog box and return the path to the selected file
	filename=os.path.basename(filename)
	#filename = str(filename)
	#print(type(filename))

	imagem = mp.leImagem(filename)
	mp.exibeImagem(imagem)
	#a = np.asarray(imagem)



if __name__ == '__main__':
	main()