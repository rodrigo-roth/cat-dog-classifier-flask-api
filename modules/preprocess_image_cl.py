from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import numpy as np
import keras

class PreprocessImage():
    
    def preprocess_image(self, image, target_size):
        """  
        Pré-processa a imagem enviada para se adequar aos parâmetros do modelo treinado.
        A imagem é convertida para o padrão de cores RGB caso já não esteja, 
        redimensionada para o tamanho usado no modelo e transforamda em array para ser lida.
        
        :param image: Imagem enviada em base64.
        """
        if image.mode != "RGB":
            image = image.convert("RGB")
        image = image.resize(target_size)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        
        return image
