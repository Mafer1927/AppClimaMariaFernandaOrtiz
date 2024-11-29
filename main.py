# librerias 
from flask import Flask,render_template, request
import requests

app = Flask(__name__)

# funciones 
def get_weather_data(city:str):
  
  
    API_KEY = '0b9eef34737575f263f08440fffa4e5b'
    idioma = 'es'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}'
    r = requests.get(url).json()
    print(r)
    return r

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', latitud='', longitud='', ciudad='', humedad='',presion='', descripcion='', icon = '' , cod = '')

    ciudad= request.form.get('txtCiudad')
    if ciudad:
        data=get_weather_data(ciudad) #lo que trae el api
        cod=data.get('cod')
        if cod != 200:
            return render_template('index.html', latitud='', longitud='', ciudad='', humedad='',presion='', descripcion='', icon = '' , cod = '')
        latitud=data.get('main').get('temp')
        longitud=data.get('coord').get('lon')
        humedad=data.get('main').get('humidity')
        presion=data.get('main').get('pressure')
        descripcion=data.get('weather')[0].get('description')
        icon=data.get('weather')[0].get('icon')
        return render_template('index.html', latitud=latitud, longitud=longitud, ciudad=ciudad.capitalize(), humedad=humedad,presion=presion, descripcion=descripcion.upper(), icon = icon , cod = cod)
    else:
        return render_template('index.html', latitud='', longitud='', ciudad='', humedad='',presion='', descripcion='', icon = '' , cod = '')

@app.route('/cv.html')
def cv():
    return render_template('cv.html')


if __name__ == "__main__":
    app.run(debug=True)