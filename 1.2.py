from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    comodos = {
        'Quarto': '/quarto',
        'Banheiro': '/banheiro'
    }
    return render_template("index.html", comodos=comodos)

@app.route('/quarto')
def quarto():
    opcoes_quarto = {
        'Sensores': '/quarto/sensores',
        'Atuadores': '/quarto/atuadores'
    }
    return render_template("quarto.html", opcoes=opcoes_quarto)

@app.route('/quarto/sensores')
def quarto_sensores():
    sensores_quarto = {
        'Sensor de Luminosidade': 1,  
        'Sensor de Temperatura': 0    
    }
    return render_template("sensors.html", sensores=sensores_quarto, comodo='Quarto')

@app.route('/quarto/atuadores')
def quarto_atuadores():
    atuadores_quarto = {
        'Interruptor de Luz': 1,
        'Ventilador': 0,
        'Cortina Automática': 1
    }
    return render_template("actuators.html", atuadores=atuadores_quarto, comodo='Quarto')

@app.route('/banheiro')
def banheiro():
    opcoes_banheiro = {
        'Sensores': '/banheiro/sensores',
        'Atuadores': '/banheiro/atuadores'
    }
    return render_template("banheiro.html", opcoes=opcoes_banheiro)

@app.route('/banheiro/sensores')
def banheiro_sensores():
    sensores_banheiro = {
        'Sensor de Umidade': 1, 
        'Sensor de Temperatura': 0 
    }
    return render_template("sensors.html", sensores=sensores_banheiro, comodo='Banheiro')

@app.route('/banheiro/atuadores')
def banheiro_atuadores():
    atuadores_banheiro = {
        'Lâmpada Inteligente': 1,
        'Exaustor': 0
    }
    return render_template("actuators.html", atuadores=atuadores_banheiro, comodo='Banheiro')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
