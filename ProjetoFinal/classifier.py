
# coding: utf-8

# In[1]:


from keras import layers
from keras.models import Model
from keras.models import load_model
from keras import metrics
from keras import callbacks
import os
import cv2
import string
import numpy as np
from matplotlib import pyplot as plt

#Init main values
symbols = string.ascii_lowercase + "0123456789" # All symbols captcha can contain
num_symbols = len(symbols)
img_shape = (50, 200, 1)
#print(symbols)


# In[2]:


# First we need to preprocess the data
def preprocess_data():
    n_samples = len(os.listdir('samples'))
    X = np.zeros((n_samples, 50, 200, 1))
    y = np.zeros((5, n_samples, num_symbols))

    for i, pic in enumerate(os.listdir('samples')):
        # Read image as grayscale
        img = cv2.imread(os.path.join('samples', pic), cv2.IMREAD_GRAYSCALE)
        '''if i == 0:
            print(img)
            #plt.imshow(img, 'gray')
         '''   
        pic_target = pic[:-4] #tira .jpg
        #print(pic_target)
        if len(pic_target) < 6:
            # Scale and reshape image
            img = img / 255. #conteúdo de 0 a 1
            img = np.reshape(img, (50, 200, 1)) #muda formato do array
            #if i == 0:
            #    print(img)
            #    plt.imshow(img, 'gray')
            
            
            # Define targets and code them using OneHotEncoding
            targs = np.zeros((5, num_symbols))
            for j, l in enumerate(pic_target):
                ind = symbols.find(l)
                targs[j, ind] = 1
            X[i] = img
            y[:, i] = targs
        #else: #talvez remover esse doido diferente
            #print(pic_target)
    
    # Return final data
    return X, y

X, y = preprocess_data()
X_train, y_train = X[:970], y[:, :970]
X_test, y_test = X[970:], y[:, 970:]


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
    flat = layers.Flatten()(mp3)
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


# In[4]:


net = create_net()
history = net.fit(X_train, [y_train[0], y_train[1], y_train[2], y_train[3], y_train[4]], 
                  batch_size=32, epochs=30, validation_split=0.2)


# In[5]:


def predict(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE) / 255.
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


# In[13]:


def accuracy(y_pred, y_true):
    
    total = len(y_pred)
    rigth = 0
    
    for i in range(0, total):
        
        if y_pred[i] == y_true[i]:
            rigth += 1
            print('pred: ' + y_pred[i] + ' true: '+ y_true[i])
            
    perc = rigth/total
    
    return perc


# In[14]:


l = os.listdir('samples')[970:]
#l
y_true = []
y_pred = []
for ele in l:
    y_target = ele[:-4]
    
    if len(y_target) < 6: #evita esse arquivo: samples/.ipynb_checkpoints <class 'NoneType'>
    
        y_true.append(y_target) 
        #print(ele)

        pred, prob = predict('samples/'+ele)
        y_pred.append(pred)
        
        #print(pred, prob)
        
print(accuracy(y_pred, y_true))


# In[9]:


# Check model on some samples
print(net.evaluate(X_test, [y_test[0], y_test[1], y_test[2], y_test[3], y_test[4]]))

print(predict('samples/8n5p3.png'))
print(predict('samples/f2m8n.png'))
print(predict('samples/dce8y.png'))
print(predict('samples/3eny7.png'))
print(predict('samples/npxb7.png'))

####outros
print(predict('samples/573bn.png'))
print(predict('samples/bm3p8.png'))

