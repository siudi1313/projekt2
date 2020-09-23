import sqlite3 as sql

if __name__ == "__main__":
    #Tworzenie tabeli
    con = sql.connect('database.db')
    print("BD otwarta")
    	
    con.execute('CREATE TABLE posty (id INTEGER PRIMARY KEY AUTOINCREMENT, tytul TEXT, autor TEXT, data_publikacji TEXT, tresc TEXT)')
    print("Tabela utworzona")
    	
    con.close()
    print("BD zamknieta")
    
    
    #Wypelnianie tabeli
    con = sql.connect('database.db')
    print("\nBD otwarta")
    	
    cur = con.cursor()
    print("Kursor otwarty")
    	
    cur.execute("INSERT INTO posty (tytul, autor, data_publikacji, tresc) VALUES (?, ?, ?, ?)", ('Smartphony godne polecenia', 'Jan Kowalski', '2020-02-11', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar urna a sem venenatis elementum. Aliquam aliquet eleifend dolor. Pellentesque et est blandit, hendrerit diam sed, feugiat risus. Sed aliquam diam sed laoreet suscipit. Vestibulum viverra dolor ante, non pellentesque justo accumsan quis. Nulla nulla eros, pharetra euismod viverra eu, accumsan quis est. Vestibulum pretium aliquet sapien, eget placerat libero convallis et. Fusce vehicula rhoncus quam nec consequat. Vivamus ac fringilla justo. Donec sodales, quam a blandit placerat, elit nulla lobortis nibh, vel ornare justo nunc et tellus. Phasellus eu velit dolor.'))
    print("Rekord dodany")
    cur.execute("INSERT INTO posty (tytul, autor, data_publikacji, tresc) VALUES (?, ?, ?, ?)", ('Jaki komputer kupić? Na co warto zwrócić uwagę?', 'Magda Nowak', '2020-04-01', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar urna a sem venenatis elementum. Aliquam aliquet eleifend dolor. Pellentesque et est blandit, hendrerit diam sed, feugiat risus. Sed aliquam diam sed laoreet suscipit. Vestibulum viverra dolor ante, non pellentesque justo accumsan quis. Nulla nulla eros, pharetra euismod viverra eu, accumsan quis est. Vestibulum pretium aliquet sapien, eget placerat libero convallis et. Fusce vehicula rhoncus quam nec consequat. Vivamus ac fringilla justo. Donec sodales, quam a blandit placerat, elit nulla lobortis nibh, vel ornare justo nunc et tellus. Phasellus eu velit dolor.'))
    print("Rekord dodany")
    cur.execute("INSERT INTO posty (tytul, autor, data_publikacji, tresc) VALUES (?, ?, ?, ?)", ('Test nowej karty graficznej od NVIDIA', 'Igor Kropka', '2020-04-22', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar urna a sem venenatis elementum. Aliquam aliquet eleifend dolor. Pellentesque et est blandit, hendrerit diam sed, feugiat risus. Sed aliquam diam sed laoreet suscipit. Vestibulum viverra dolor ante, non pellentesque justo accumsan quis. Nulla nulla eros, pharetra euismod viverra eu, accumsan quis est. Vestibulum pretium aliquet sapien, eget placerat libero convallis et. Fusce vehicula rhoncus quam nec consequat. Vivamus ac fringilla justo. Donec sodales, quam a blandit placerat, elit nulla lobortis nibh, vel ornare justo nunc et tellus. Phasellus eu velit dolor.'))
    print("Rekord dodany")
    cur.execute("INSERT INTO posty (tytul, autor, data_publikacji, tresc) VALUES (?, ?, ?, ?)", ('Najgorsze programy i systemy', 'Wiktoria Konieczna', '2020-05-10', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar urna a sem venenatis elementum. Aliquam aliquet eleifend dolor. Pellentesque et est blandit, hendrerit diam sed, feugiat risus. Sed aliquam diam sed laoreet suscipit. Vestibulum viverra dolor ante, non pellentesque justo accumsan quis. Nulla nulla eros, pharetra euismod viverra eu, accumsan quis est. Vestibulum pretium aliquet sapien, eget placerat libero convallis et. Fusce vehicula rhoncus quam nec consequat. Vivamus ac fringilla justo. Donec sodales, quam a blandit placerat, elit nulla lobortis nibh, vel ornare justo nunc et tellus. Phasellus eu velit dolor.'))
    print("Rekord dodany")
    con.commit()
    	
    cur.execute("SELECT * FROM posty")
    print(cur.fetchall())
    	
    cur.close()
    print("Kursor zamkniety")

    con.close()
    print("BD zamknieta")


    #Tworzenie tabeli
    con = sql.connect('database.db')
    print("\n\nBD otwarta")
    	
    con.execute('CREATE TABLE uzytkownicy (id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, haslo TEXT, nazwa TEXT, email TEXT)')
    print("Tabela utworzona")
    	
    con.close()
    print("BD zamknieta")

    #Wypelnianie tabeli
    con = sql.connect('database.db')
    print("\nBD otwarta")
    	
    cur = con.cursor()
    print("Kursor otwarty")
    	
    cur.execute("INSERT INTO uzytkownicy (login, haslo, nazwa, email) VALUES (?, ?, ?, ?)", ('login_konieczna', 'haslo_konieczna', 'Wiktoria Konieczna', 'konieczna@email.com'))
    print("Rekord dodany")
    cur.execute("INSERT INTO uzytkownicy (login, haslo, nazwa, email) VALUES (?, ?, ?, ?)", ('login_kowalski', 'haslo_kowalski', 'Jan Kowalski', 'konieczna@email.com'))
    print("Rekord dodany")
    cur.execute("INSERT INTO uzytkownicy (login, haslo, nazwa, email) VALUES (?, ?, ?, ?)", ('login_nowak', 'haslo_nowak', 'Magda Nowak', 'konieczna@email.com'))
    print("Rekord dodany")
    con.commit()
    	
    cur.execute("SELECT * FROM uzytkownicy")
    print(cur.fetchall())
    	
    cur.close()
    print("Kursor zamkniety")

    con.close()
    print("BD zamknieta")