# utilizzo del microframework flask per creare un app che stampa HelloWorld

from flask import Flask

app = Flask(__name__)  # creazione istanza webapp

@app.route("/") # decoratore che permette di chiamre la funz
def index(): # view function, logica di cosa deve succedere arrivati qui
    return "<h1>Hello World</h1>"

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, %s</h1>" %name


# server startup
if __name__ == "__main__":
    app.run(debug= True) # avvio il server integrato in python

# -1 Arriva una richiesta dal browser all'indirizzo /.
# -2 Flask controlla la sua mappa interna (creata con @app.route).
# -3 Vede che / corrisponde alla funzione hello_world.
# -4 Esegue la funzione.
# -5 Prende il return, lo impacchetta in una risposta HTTP valida e 
#    lo spedisce al browser.
