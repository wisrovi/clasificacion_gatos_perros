import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

model = tf.keras.models.load_model("modelo/model.h5")
# model.summary()


def convertir_imagen_numpy(nombre_imagen):
    img = image.load_img(nombre_imagen, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    return images


def predict(nombre_imagen):
    imagen = convertir_imagen_numpy(nombre_imagen)
    rta = model.predict(imagen)
    if rta[0] > 0.5:
        return "DOG"
    else:
        return "CAT"


if __name__ == "__main__":
    rta = predict("recibido.jpg")
    print(rta)