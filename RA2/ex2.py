from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>Minha Casa Conectada</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
                h2 {
                    font-size: 2em;
                }
                ul {
                    list-style-type: none;
                }
                ul li {
                    margin: 10px 0;
                }
                a {
                    text-decoration: none;
                    color: purple;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <h2>Minha Casa Conectada</h2>
            <h3>Escolha um cômodo:</h3>
            <ul>
                <li><a href="/quarto">Quarto</a></li>
                <li><a href="/banheiro">Banheiro</a></li>
            </ul>
        </body>
    </html>
    """

@app.route('/quarto')
def quarto():
    return """
    <html>
        <head>
            <title>Quarto</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
                a {
                    text-decoration: none;
                    color: purple;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <h1>Quarto</h1>
            <ul>
                <li><a href="/quarto/sensores">Sensores</a></li>
                <li><a href="/quarto/atuadores">Atuadores</a></li>
            </ul>
            <p>Voltar para <a href="/">página inicial</a>.</p>
        </body>
    </html>
    """ 

@app.route('/quarto/sensores')
def quarto_sensores():
    return """
    <html>
        <head>
            <title>Sensores do Quarto</title>
        </head>
        <body>
            <h1>Sensores do Quarto</h1>
            <ul>
                <li>Sensor de Luminosidade</li>
            </ul>
            <p>Voltar para <a href="/quarto">Quarto</a>.</p>
        </body>
    </html>
    """
@app.route('/quarto/atuadores')
def quarto_atuadores():
    return """
    <html>
        <head>
            <title>Atuadores do Quarto</title>
        </head>
        <body>
            <h1>Atuadores do Quarto</h1>
            <ul>
                <li>Interruptor de Luz</li>
            </ul>
            <p>Voltar para <a href="/quarto">Quarto</a>.</p>
        </body>
    </html>
    """
@app.route('/banheiro')
def banheiro():
    return """
    <html>
        <head>
            <title>Banheiro</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
                a {
                    text-decoration: none;
                    color: purple;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <h1>Banheiro</h1>
            <ul>
                <li><a href="/banheiro/sensores">Sensores</a></li>
                <li><a href="/banheiro/atuadores">Atuadores</a></li>
            </ul>
            <p>Voltar para <a href="/">página inicial</a>.</p>
        </body>
    </html>
    """

@app.route('/banheiro/sensores')
def banheiro_sensores():
    return """
    <html>
        <head>
            <title>Sensores do Banheiro</title>
        </head>
        <body>
            <h1>Sensores do Banheiro</h1>
            <ul>
                <li>Sensor de Umidade</li>
            </ul>
            <p>Voltar para <a href="/banheiro">Banheiro</a>.</p>
        </body>
    </html>
    """

@app.route('/banheiro/atuadores')
def banheiro_atuadores():
    return """
    <html>
        <head>
            <title>Atuadores do Banheiro</title>
        </head>
        <body>
            <h1>Atuadores do Banheiro</h1>
            <ul>
                <li>Lâmpada Inteligente</li>
            </ul>
            <p>Voltar para <a href="/banheiro">Banheiro</a>.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
