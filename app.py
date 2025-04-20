from flask import Flask, render_template
from static.script.CaptacaoDeValores import obter_e_exibir_valores

app = Flask(__name__)

@app.route('/')
def index():
    dolar, euro = obter_e_exibir_valores()
    return render_template('index.html', dolar=dolar, euro=euro)

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
