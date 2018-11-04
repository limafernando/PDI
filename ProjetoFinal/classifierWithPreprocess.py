
# coding: utf-8

# In[5]:


import os
import string

import cv2
import numpy as np
from matplotlib import pyplot as plt

from keras import layers
from keras.models import Model
from keras.models import load_model
from keras import metrics
from keras import callbacks

#Init main values
symbols = string.ascii_lowercase + "0123456789" # All symbols captcha can contain
num_symbols = len(symbols)
img_shape = (50, 200, 1)

kernel1 = np.ones((3,3), np.uint8) #used for dilation and erosion
kernel2 = np.ones((3,1), np.uint8) #used for dilation in the vertical

from keras.utils import plot_model


# In[2]:


def uAdaptativeThresholding():
    n_samples = len(os.listdir('samples'))
    X = np.zeros((n_samples, 50, 200, 1))
    y = np.zeros((5, n_samples, num_symbols))

    for i, pic in enumerate(os.listdir('samples')):
        
        pic_target = pic[:-4] #tira .jpg
        
        # Read image as grayscale
        img = cv2.imread(os.path.join('samples', pic), cv2.IMREAD_GRAYSCALE)
        
        #print(img)
        
       
        if len(pic_target) < 6:
        
            img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 2) #thresholding
            img = cv2.dilate(img, kernel1, iterations=1)
            img = cv2.erode(img, kernel1, iterations=1)
            img = cv2.dilate(img, kernel2, iterations=1)
        
            # Scale and reshape image
            img = img / 255. #conteúdo de 0 a 1
            img = np.reshape(img, (50, 200, 1)) #muda formato do array para o formato de X
            
            # Define targets and code them using OneHotEncoding
            targs = np.zeros((5, num_symbols))
            
            for j, l in enumerate(pic_target): #percorre cada caracter da string
                
                ind = symbols.find(l)
                targs[j, ind] = 1
            
            X[i] = img
            y[:, i] = targs
    
    # Return final data
    return X, y


# In[3]:


def uOtsuThresholding():
    
    n_samples = len(os.listdir('samples'))
    X = np.zeros((n_samples, 50, 200, 1))
    y = np.zeros((5, n_samples, num_symbols))

    for i, pic in enumerate(os.listdir('samples')):
        
        pic_target = pic[:-4] #tira .jpg
        
        # Read image as grayscale
        img = cv2.imread(os.path.join('samples', pic), cv2.IMREAD_GRAYSCALE)
        
        if len(pic_target) < 6:
        
            ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #OtsuThresholding
            img = cv2.dilate(img, kernel1, iterations=1)
            img = cv2.erode(img, kernel1, iterations=1)
            img = cv2.dilate(img, kernel2, iterations=1)

            '''if pic_target == '226md':
                plt.imshow(img, 'gray')'''

            # Scale and reshape image
            img = img / 255. #conteúdo de 0 a 1
            img = np.reshape(img, (50, 200, 1)) #muda formato do array
            
            # Define targets and code them using OneHotEncoding
            targs = np.zeros((5, num_symbols))
            
            for j, l in enumerate(pic_target):
                
                ind = symbols.find(l)
                targs[j, ind] = 1
            
            X[i] = img
            y[:, i] = targs
    
    # Return final data
    return X, y


# In[4]:


def uBlurOtsuThresholding():
    n_samples = len(os.listdir('samples'))
    X = np.zeros((n_samples, 50, 200, 1))
    y = np.zeros((5, n_samples, num_symbols))

    for i, pic in enumerate(os.listdir('samples')):
        
        pic_target = pic[:-4] #tira .jpg
        
        # Read image as grayscale
        img = cv2.imread(os.path.join('samples', pic), cv2.IMREAD_GRAYSCALE)
       
        if len(pic_target) < 6:
            
            blur = cv2.GaussianBlur(img, (5, 5), 0)
            ret, img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #blurOtsuThresholding
            img = cv2.dilate(img, kernel1, iterations=1)
            img = cv2.erode(img, kernel1, iterations=1)
            img = cv2.dilate(img, kernel2, iterations=1)
            
            # Scale and reshape image
            img = img / 255. #conteúdo de 0 a 1
            img = np.reshape(img, (50, 200, 1)) #muda formato do array
            
            # Define targets and code them using OneHotEncoding
            targs = np.zeros((5, num_symbols))
            
            for j, l in enumerate(pic_target):
                
                ind = symbols.find(l)
                targs[j, ind] = 1
            
            X[i] = img
            y[:, i] = targs
    
    # Return final data
    return X, y


# In[3]:


# Define a function that creates a net
def create_net():
    
    img = layers.Input(shape=img_shape) # Get image as an input and process it through some Convs
    
    conv1 = layers.Conv2D(16, (3, 3), padding='same', activation='relu')(img)
    
    mp1 = layers.MaxPooling2D(padding='same')(conv1)  # 100x25
    
    conv2 = layers.Conv2D(32, (3, 3), padding='same', activation='relu')(mp1)
    
    mp2 = layers.MaxPooling2D(padding='same')(conv2)  # 50x13
    
    conv3 = layers.Conv2D(32, (3, 3), padding='same', activation='relu')(mp2)
    
    bn = layers.BatchNormalization()(conv3)
    
    mp3 = layers.MaxPooling2D(padding='same')(bn)  # 25x7
    
    # Get flattened vector and make 5 branches from it. Each branch will predict one letter
    flat = layers.Flatten()(mp3) #array 25*7=175
    
    outs = []
    for _ in range(5):
        dens1 = layers.Dense(64, activation='relu')(flat)
        drop = layers.Dropout(0.5)(dens1)
        res = layers.Dense(num_symbols, activation='sigmoid')(drop)

        outs.append(res)
    
    # Compile model and return it
    model = Model(img, outs)
    model.compile('rmsprop', loss=['categorical_crossentropy', 'categorical_crossentropy',
                                   'categorical_crossentropy', 'categorical_crossentropy', 'categorical_crossentropy'])
    return model


# In[6]:


def predictAT(filepath):
    
    #print(filepath)
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    #print(type(img))
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 2) #thresholding
    img = cv2.dilate(img, kernel1, iterations=1)
    img = cv2.erode(img, kernel1, iterations=1)
    img = cv2.dilate(img, kernel2, iterations=1) / 255.
    
    res = np.array(net.predict(img[np.newaxis, :, :, np.newaxis]))
    
    ans = np.reshape(res, (5, 36))
    l_ind = []
    probs = []
    for a in ans:
        l_ind.append(np.argmax(a))
        probs.append(np.max(a))

    capt = ''
    for l in l_ind:
        capt += symbols[l]
        
    return capt, sum(probs) / 5


# In[7]:


def predictOT(filepath):
    
    #print(filepath)
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    #print(type(img))
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #OtsuThresholding
    img = cv2.dilate(img, kernel1, iterations=1)
    img = cv2.erode(img, kernel1, iterations=1)
    img = cv2.dilate(img, kernel2, iterations=1)/ 255.
    res = np.array(net.predict(img[np.newaxis, :, :, np.newaxis]))
    ans = np.reshape(res, (5, 36))
    l_ind = []
    probs = []
    for a in ans:
        l_ind.append(np.argmax(a))
        probs.append(np.max(a))

    capt = ''
    for l in l_ind:
        capt += symbols[l]
        
    return capt, sum(probs) / 5


# In[8]:


def predictBOT(filepath):
    
    #print(filepath)
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    #print(type(img))
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret, img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #blurOtsuThresholding
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 2) #thresholding
    img = cv2.dilate(img, kernel1, iterations=1)
    img = cv2.erode(img, kernel1, iterations=1)
    img = cv2.dilate(img, kernel2, iterations=1)/ 255.
    res = np.array(net.predict(img[np.newaxis, :, :, np.newaxis]))
    ans = np.reshape(res, (5, 36))
    l_ind = []
    probs = []
    for a in ans:
        l_ind.append(np.argmax(a))
        probs.append(np.max(a))

    capt = ''
    for l in l_ind:
        capt += symbols[l]
        
    return capt, sum(probs) / 5


# In[9]:


def accuracy(y_pred, y_true):
    
    total = len(y_pred)
    rigth = 0
    
    for i in range(0, total):
        
        if y_pred[i] == y_true[i]:
            rigth += 1
            print('pred: ' + y_pred[i] + ' true: '+ y_true[i])
            
    perc = rigth/total
    
    return perc


# In[10]:


X, y = uAdaptativeThresholding()
X_train, y_train = X[:970], y[:, :970]
X_test, y_test = X[970:], y[:, 970:]

net = create_net()

history = net.fit(X_train, [y_train[0], y_train[1], y_train[2], y_train[3], y_train[4]], 
                  batch_size=32, epochs=30, validation_split=0.2)

test = os.listdir('samples')[970:]

y_true = []
y_pred = []

for ele in test:
    
    y_target = ele[:-4]
    
    if len(y_target) < 6: #evita esse arquivo: samples/.ipynb_checkpoints <class 'NoneType'>
    
        y_true.append(y_target) 
        #print(ele)

        pred, prob = predictAT('samples/'+ele)
        y_pred.append(pred)
        
        #print(pred, prob)
    
#print(y_true[-1])

print('Evaluate: ', net.evaluate(X_test, [y_test[0], y_test[1], y_test[2], y_test[3], y_test[4]]))
print('Accuracy: ', accuracy(y_pred, y_true))


# In[11]:


X, y = uOtsuThresholding()
X_train, y_train = X[:970], y[:, :970]
X_test, y_test = X[970:], y[:, 970:]

net = create_net()
history = net.fit(X_train, [y_train[0], y_train[1], y_train[2], y_train[3], y_train[4]], 
                  batch_size=32, epochs=30, validation_split=0.2)

test = os.listdir('samples')[970:]

y_true = []
y_pred = []

for ele in test:
    
    y_target = ele[:-4]
    
    if len(y_target) < 6: #evita esse arquivo: samples/.ipynb_checkpoints <class 'NoneType'>
    
        y_true.append(y_target) 
        #print(ele)

        pred, prob = predictOT('samples/'+ele)
        y_pred.append(pred)
        
        #print(pred, prob)
    
#print(y_true[-1])

print('Evaluate: ', net.evaluate(X_test, [y_test[0], y_test[1], y_test[2], y_test[3], y_test[4]]))
print('Accuracy: ', accuracy(y_pred, y_true))


# In[12]:


X, y = uBlurOtsuThresholding()
X_train, y_train = X[:970], y[:, :970]
X_test, y_test = X[970:], y[:, 970:]

net = create_net()
history = net.fit(X_train, [y_train[0], y_train[1], y_train[2], y_train[3], y_train[4]], 
                  batch_size=32, epochs=30, validation_split=0.2)

test = os.listdir('samples')[970:]

y_true = []
y_pred = []

for ele in test:
    
    y_target = ele[:-4]
    
    if len(y_target) < 6: #evita esse arquivo: samples/.ipynb_checkpoints <class 'NoneType'>
    
        y_true.append(y_target) 
        #print(ele)

        pred, prob = predictBOT('samples/'+ele)
        y_pred.append(pred)
        
        #print(pred, prob)
    
#print(y_true[-1])

print('Evaluate: ', net.evaluate(X_test, [y_test[0], y_test[1], y_test[2], y_test[3], y_test[4]]))
print('Accuracy: ', accuracy(y_pred, y_true))

