from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    panas = ['Kevin', 'Marco', 'Sergio', 'Ronald', 
    'Hector', 'Cabana', 'Samir',
    'Toto', 'Sasu', 'Richi', 
    'Robert', 'Zahid', 'Migue',
    'Pipe', 'Comandante', 'Mateo',
    'Chucho']
    data = {
        'titulo':'Listado Panas',
        'bienvenida': 'Hello there',
        'panas': panas,
        'No_Pana':len(panas)
    }
    return render_template("index.html", data = data, body = panas)
    # return "<h1>¡Hello world, sigo mejorando día tras día!</h1>"


if __name__ == '__main__':
    app.run(debug=True, port=5000)




