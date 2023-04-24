import pickle
import json
import random
# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse


from model import get_recommended_products
from utils import (
    product_names_mapping,
    properties_mapping,
    allowed_values_countries,
    allowed_values_gender,
    allowed_values_relation_type,
    allowed_values_activity_level,
    allowed_values_segment
)

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class RecommendProducts(Resource):
    # Corresponds to POST request
    def post(self):

        # Validation rules of request data
        parser = reqparse.RequestParser()
        parser.add_argument(
            'country_of_residence',
            required=True,
            choices=allowed_values_countries,
            help=f'Bad choice. Valid choices are: {allowed_values_countries}'
        )
        parser.add_argument(
            'gender',
            required=True,
            choices=allowed_values_gender,
            help=f'Bad choice. Valid choices are: {allowed_values_gender}'
        )
        parser.add_argument('age', required=True)
        parser.add_argument('seniority_level', required=True)       
        parser.add_argument(
            'relation_type',
            required=True,
            choices=allowed_values_relation_type,
            help=f'Bad choice. Valid choices are: {allowed_values_relation_type}'
        )
        parser.add_argument('province_name', required=True)
        parser.add_argument(
            'activity_level',
            required=True,
            choices=allowed_values_activity_level,
            help=f'Bad choice. Valid choices are: {allowed_values_activity_level}'
        )
        parser.add_argument('annual_income', required=True)
        parser.add_argument(
            'segment',
            required=True,
            choices=allowed_values_segment,
            help=f'Bad choice. Valid choices are: {allowed_values_segment}'
        )

        args = parser.parse_args()

        # dummy / static data for some fields (that are not collected through the API)
        input_data = {
            'fecha_dato': '2016-06-28',
            'ncodpers': str(random.randint(10000, 100000)),
            'ind_empleado': 'N',
            'fecha_alta': '2013-08-28',
            'ind_nuevo': '0',
            'antiguedad': '34',
            'indrel': '1',
            'indrel_1mes': '3',
            'indresi': 'S',
            'indext': 'N',
            'conyuemp': 'S',
            'canal_entrada': 'KHS',
            'indfall': 'S',
            'tipodom': '1',
            'cod_prov': '15'
        }

        # Collect request data
        for key, value in json.loads(request.data).items():
            try:
                property_name = properties_mapping[key]
                input_data.update({property_name: str(value)})
            except KeyError:
                continue
        
        # Serve data to ML model and get recommendations
        recommended_products = get_recommended_products(input_data)
        response = {'recommended_products': []}
        for product in recommended_products:
            response['recommended_products'].append(product_names_mapping[product])

        return jsonify(response)


# adding the defined resources along with their corresponding urls
api.add_resource(RecommendProducts, '/recommend')

if __name__ == '__main__':
    app.run()