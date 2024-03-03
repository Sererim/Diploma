from flask import Flask, request, jsonify
from flask_restful import Api

from utils import predict_image, get_data, get_response


app = Flask(__name__)
api = Api(app)
# app.debug = True


@app.route('/')
def index():
    return "TEST"


@app.route('/image', methods=['POST'])
def get_image():
    try:
        image_file = request.files['image']
        prediction = predict_image(image_file)
        data = get_data(food_id=prediction.item())
        if len(data) != 0:
            response = {
                'status' : 'success',
            }
            response.update(get_response(data, food_id=prediction.item()))    
        else:
            response = {
                'status' : 'success',
                'food' : 'unknown'
            }
        return jsonify(response)
    except Exception as e:
        response = {
            'status' : 'error',
            'message': str(e)
        }
        return jsonify(response)


if __name__ == '__main__':
    app.run()
