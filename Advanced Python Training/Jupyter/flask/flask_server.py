# Here we build a Flask microservice to respond tio HTTP requests to specific routes
import requests
from flask import Flask, jsonify
from flask import render_template
from WeatherService.weather_service import getWeather


# CAUTION: Flask is a development server, NOT production
# for production, combine Flask with a WSGI-compliant server (Tomcat, Apache...)
# Recommended for security etc.

def main():
    '''here is a simple Flask implementation'''
    app = Flask(__name__)
    # we then declare routes for our web server

    @app.route('/') # this is the top level of our server
    def root():
        return 'Welcome'

    @app.route('/hello')
    def hello():
        return '<h3>Hello</h3>'

    # sometimes we need several ways to access the same content
    @app.route('/info')
    @app.route('/about')
    @app.route('/stuff')
    def generic():
        return 'this is info about stuff'

    # we may pass URL parameters to our routing
    @app.route('/greet') # allow the possibility of no person parameter
    @app.route('/greet/<person>') # <> means read a parameter
    def greet(person='Friend'):
        if person:
            return f'<h3>Welcome {person}'
        else:
            return 'Welcome to tis Flask server'

    # we may return an HTML template
    @app.route('/lunch')
    @app.route('/lunch/<dessert>')
    def lunch(dessert=None):
        return render_template('lunch.html', dessert=dessert)

    @app.route('/swapi')
    @app.route('/swapi/<category>/<id>')
    def swapi(category = 'planets', id = 1):
        swapi_url = f"https://swapi.dev/api/{category}/{id}"

        response = requests.get(swapi_url)

        if response.status_code == 200:
            data = response.json()
            # return jsonify(data)
            # return data
            return render_template('swapi.html', data=data, category=category, id=id)
        else:
            # return jsonify({'error message': 'Resource not found'}), 404
            return render_template('swapi.html', data=None, category=None, id=None)

    @app.route('/get_weather/<city>')
    def get_weather(city='Athlone'):

        weatherDetails = getWeather(city)

        if weatherDetails['cod'] == '200':
            return render_template('weather.html', data=weatherDetails, city=city)
        else:
            # return jsonify({'error message': 'Resource not found'}), 404
            return render_template('weather.html', data=None, city=city)

    # we must remember to start the server
    app.run()

if __name__ == '__main__':
    main()
