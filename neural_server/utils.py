from urllib import response
import tensorflow as tf
from keras import models
from numpy import argmax
from PIL import Image
import sqlite3

names = ['food', 'vitamin_d', 'vitamin_c', 'vitamin_e', 'vitamin_a',
         'vitamin_b6', 'vitamin_l', 'magnesium', 'calcium', 'zinc',
         'potassium', 'iron', 'iodine', 'folate', 'carbohydrates',
         'fats', 'proteins']


def preprocess_image(image):
    """
    Function to preprocess the image and convert it to a correct format.

    Args:
        image: any image format
    Returns:
        _type_: processed image in tensorflow format.
    """
    image = tf.cast(tf.image.resize(image, (224, 224)), dtype=tf.float32) / 255.0
    image = tf.expand_dims(image, axis=0)
    
    return image


def predict_image(image_file):
    """
    Function to predict class of food using image.
    Args:
        image_file (_type_): image from POST request.
    Returns:
        _type_: food class
    """
    image = Image.open(image_file)
    image = preprocess_image(image)
    
    model = models.load_model(filepath="Neural net\\model.h5")
    prediction = argmax(model.predict(image))
    
    return prediction


def get_data(food_id: int):
    """
    Function that reads data from Food.db and sends out all data.
    args:
        food_id (int): predicted id of food. NOTE not all food has place in database.
    """
    connection = sqlite3.connect("database/Food.db")
    cursor = connection.cursor()
    
    cursor.execute("""SELECT * FROM food \
    JOIN food_vitamins ON food.food_id = food_vitamins.food_id \
    JOIN food_nutrients ON food.food_id = food_nutrients.food_id \
    WHERE food.food_id=? """, (food_id,))
    rows = cursor.fetchall()
    return rows[0]


def get_response(data, food_id: int):
    data = [i for i in data if i != food_id]
    response = {}
    for i, item in enumerate(data):
        response[names[i]] = item
    return response

if __name__ == '__main__':
    print(get_data(food_id=44)[0])
    print(get_response((44, 'fried_rice', 44, 0.0, 0.0032, 0.00017, 1.9999999999999998e-05, 6.4e-05, 3e-06, 0.012, 0.012, 0.00083, 0.1, 0.0005, 0.0, 6e-06, 44, 27.6, 3.66, 7.28), food_id=44))
    