from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    @staticmethod
    def lettura_dabatase_museo():
        """Leggo tutti i dati del database Museo"""
        results = []
        cnx= ConnessioneDB.get_connection()
        if cnx is None:
            print("Connessione Fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM museo")
            for row in cursor:
                museo = Museo(**row)
                results.append(museo)
            cursor.close()
            cnx.close()
            return results



    # TODO
