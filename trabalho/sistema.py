import numpy as np
from PIL import Image

imagem = Image.open('CNN1.png')
imagem.show()
a = np.asarray(imagem)
#print(len(a[0]))
#len(a) == qtd linhas
#len(a[0]) == qtd colunas
#len(a[0][0]) == qtd componentes do pixel
#a[0][0][0] == acesso componento do pixel



'''print(a[0][0][0])
pixel1 = a[0][0]
print(pixel1)
print('r:', pixel1[0])
print('g:', pixel1[1])
print('b:', pixel1[2])'''

