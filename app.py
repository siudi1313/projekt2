from flask import Flask, render_template, request, redirect, url_for, request, abort
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import sqlite3 as sql
from datetime import date

app = Flask(__name__)

app.config.update( 
    DEBUG = True,
    SECRET_KEY = 'klucz_sekret'
)

login_manager = LoginManager() 
login_manager.init_app(app) 
login_manager.login_view = "login" 

class User(UserMixin): 
    name = "NULL"

    def __init__(self, id): 
        self.id = id

@app.route("/login", methods=["GET", "POST"]) 
def login(): 
    if request.method == 'POST':
        con = sql.connect('database.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM uzytkownicy")
        uzytkownicy = cur.fetchall()
        cur.close()
        con.close()
        login = request.form['login']
        haslo = request.form['haslo']
        for uzytkownik in uzytkownicy:
            if login == uzytkownik["login"] and haslo == uzytkownik["haslo"]:
                User.name = uzytkownik["nazwa"]
                user = User(uzytkownik["id"])
                login_user(user)
                return redirect(url_for("panel"))
        else: 
            return abort(401)
    else: 
        return render_template('login_form.html')

@app.route("/logout") 
@login_required 
def logout(): 
    logout_user()
    return render_template('rezultat.html', msg = "Zostałeś poprawnie wylgowany", tytul = "Rezultat")

@app.errorhandler(401) 
def page_not_found(e):
    return render_template('rezultat.html', msg = "Nieprawidłowe dane logowania", tytul = "Rezultat")

@login_manager.user_loader 
def load_user(user_id): 
    return User(user_id) 

@app.route("/")
def main():
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM posty ORDER BY data_publikacji DESC")
    posty = cur.fetchall()
    cur.close()
    con.close()
    return render_template('index.html', posty = posty, tytul = "Najnowsze posty")

@app.route("/info")
def info():
    return render_template('info.html', tytul = "Informacje o blogu | Kontakt")

@app.route("/prywatnosc")
def prywatnosc():
    return render_template('prywatnosc.html', tytul = "Polityka prywatności")

@app.route("/panel")
@login_required
def panel():
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM posty")
    posty = cur.fetchall()
    cur.execute("SELECT * FROM uzytkownicy")
    uzytkownicy = cur.fetchall()
    cur.close()
    con.close()
    return render_template('panel.html', posty = posty, uzytkownicy = uzytkownicy, tytul = "Panel administracyjny")

@app.route('/addPost', methods = ['POST', 'GET'])
def addPost():
    if request.method == 'POST':
        try:
            tytul = request.form['tytul']
            autor = request.form['autor']
            tresc = request.form['tresc']
            dzisiaj = date.today()
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO posty (tytul, autor, data_publikacji, tresc) VALUES (?, ?, ?, ?)", (tytul, autor, dzisiaj, tresc))
                con.commit()
                msg = "Sukces. Post został dodany!"
        except:
            con.rollback()
            msg = "Błąd. Post nie został dodany!"
        finally:
            return render_template("rezultat.html", msg = msg, tytul = "Rezultat")
            cur.close()
            con.close()

@app.route('/delPost', methods = ['POST', 'GET'])
def delPost():
    if request.method == 'POST':
        try:
            id = request.form['id']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM posty WHERE ID = ?", (id))
                con.commit()
                msg = "Sukces. Post został usunięty!"
        except:
            con.rollback()
            msg = "Błąd. Post nie został usunięty!"
        finally:
            return render_template("rezultat.html", msg = msg, tytul = "Rezultat")
            cur.close()
            con.close()

@app.route('/logowanie', methods = ['POST', 'GET'])
def logowanie():
    return render_template("login_form.html", tytul = "Formularz logowania")

@app.route('/rejestracja', methods = ['POST', 'GET'])
def rejestracja():
    return render_template("rejestracja_form.html", tytul = "Formularz rejestracji")

@app.route('/addUser', methods = ['POST', 'GET'])
def addUser():
    if request.method == 'POST':
        try:
            login = request.form['login']
            haslo = request.form['haslo']
            nazwa = request.form['nazwa']
            email = request.form['email']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO uzytkownicy (login, haslo, nazwa, email) VALUES (?, ?, ?, ?)", (login, haslo, nazwa, email))
                con.commit()
                msg = "Sukces. Użytkownik został dodany!"
        except:
            con.rollback()
            msg = "Błąd. Użytkownik nie został dodany!"
        finally:
            return render_template("rezultat.html", msg = msg, tytul = "Rezultat")
            cur.close()
            con.close()

@app.route('/delUser', methods = ['POST', 'GET'])
def delUser():
    if request.method == 'POST':
        try:
            id = request.form['id']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM uzytkownicy WHERE ID = ?", (id))
                con.commit()
                msg = "Sukces. Użytkownik został usunięty!"
        except:
            con.rollback()
            msg = "Błąd. Użytkownik nie został usunięty!"
        finally:
            return render_template("rezultat.html", msg = msg, tytul = "Rezultat")
            cur.close()
            con.close()

if __name__ == "__main__":
    app.run()