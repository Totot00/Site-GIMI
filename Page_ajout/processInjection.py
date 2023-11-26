"""""
import sys
import mysql.connector

# Récupération des arguments depuis PHP
patientName = sys.argv[1]
room = sys.argv[2]
medication = sys.argv[3]
flowRate = sys.argv[4]
volume = sys.argv[5]

try:
    # Connexion à la base de données
    conn = mysql.connector.connect(
        host="localhost",  # Remplacez par votre vrai host
        user="root",  # Remplacez par votre vrai utilisateur
        password="",  # Remplacez par votre vrai mot de passe
        database="hi"  # Remplacez par le nom de votre base de données
    )

    cursor = conn.cursor()

    # Préparation de la requête SQL
    query = ("INSERT INTO ajout_injec (patientname, room, medication, flowrate, volume) "
             "VALUES (%s, %s, %s, %s, %s)")

    data = (patientName, room, medication, flowRate, volume)

    # Exécution de la requête
    cursor.execute(query, data)

    # Validation de la transaction
    conn.commit()

    print("Injection ajoutée avec succès!")  # Ce message sera renvoyé à PHP et affiché à l'utilisateur

except mysql.connector.Error as err:
    print(f"Erreur de base de données: {err}")
except Exception as e:
    print(f"Erreur générale: {e}")
finally:
    # Assurez-vous de toujours fermer la connexion, même en cas d'erreur.
    cursor.close()
    conn.close()
"""

import sys
import mysql.connector

# Récupération des arguments depuis PHP
patientName = sys.argv[1]
room = sys.argv[2]
medication = sys.argv[3]
flowRate = float(sys.argv[4])  # Convertir en float pour le calcul
volume = float(sys.argv[5])  # Convertir en float pour le calcul

try:
    # Connexion à la base de données
    conn = mysql.connector.connect(
        host="localhost",  # Remplacez par votre vrai host
        user="root",  # Remplacez par votre vrai utilisateur
        password="",  # Remplacez par votre vrai mot de passe
        database="hi"  # Remplacez par le nom de votre base de données
    )

    cursor = conn.cursor()

    # Préparation de la requête SQL pour ajouter une injection
    query_injection = ("INSERT INTO ajout_injec (patientname, room, medication, flowrate, volume) "
                       "VALUES (%s, %s, %s, %s, %s)")

    data_injection = (patientName, room, medication, flowRate, volume)
    
    # Exécution de la requête pour ajouter une injection
    cursor.execute(query_injection, data_injection)

    # Calcul de alarm_time
    alarm_time = volume / flowRate

    # Préparation de la requête SQL pour ajouter une alarme
    query_alarm = ("INSERT INTO alarmes (fullname, room, alarm_time, severity) "
                   "VALUES (%s, %s, %s, %s)")

    data_alarm = (patientName, room, alarm_time, "minor")

    # Exécution de la requête pour ajouter une alarme
    cursor.execute(query_alarm, data_alarm)

    # Validation de la transaction
    conn.commit()

    print("Injection et alarme ajoutées avec succès!")  # Ce message sera renvoyé à PHP et affiché à l'utilisateur

except mysql.connector.Error as err:
    print(f"Erreur de base de données: {err}")
except Exception as e:
    print(f"Erreur générale: {e}")
finally:
    # Assurez-vous de toujours fermer la connexion, même en cas d'erreur.
    cursor.close()
    conn.close()
