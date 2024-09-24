from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
        <body>
            <h2>Minha Casa</h2>
            <h3>Acesse o menu:</h3>
            <ul>
                <li><a href="/sensors">Listar Sensores</a></li>
                <li><a href="/actuators">Listar Atuadores</a></li>
            </ul>
        </body>
    </html>
    """

@app.route('/sensors')
def sensors():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
        <body>
            <h1>Sensores</h1>
            <ul>
                <li>Sensor de Umidade</li>
                <li>Sensor de Temperatura</li>
                <li>Sensor de Luminosidade</li>
            </ul>
            <p>Voltar para <a href="/">página inicial</a>!</p>
        </body>
    </html>
    """

@app.route('/actuators')
def actuators():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
                h1 {
                    font-size: 2em;
                }
                p a {
                    color: purple;
                }
                p a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <h1>Atuadores</h1>
            <ul>
                <li>Servo Motor</li>
                <li>Lâmpada</li>
            </ul>
            <p>Voltar para <a href="/">página inicial</a>!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
