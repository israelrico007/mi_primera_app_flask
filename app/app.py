from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    #return "¡Hola, mundo!"
    return render_template('home.html')

@app.route('/about')
def about():
    return "Acerca de nosotros"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
