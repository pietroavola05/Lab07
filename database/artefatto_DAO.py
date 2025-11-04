from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    @staticmethod
    def filtraggio_museo_epoca_artefatti(museo_richiesto, epoca_selezionata):
        """Restituisco la lista degli artefatti filtrata in base al museo di appartenenza"""
        print("Sono nel DAO")
        results = []
        cnx= ConnessioneDB.get_connection()
        if cnx is None:
            print("Connessione Fallita")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            print("Sto per fare la query d filtraggio")
            print(museo_richiesto)
            print(epoca_selezionata)
            #ricevo come parametri l'id del museo richiesto e l'epoca selezionata e faccio un filtraggio nella where
            query = "SELECT * FROM artefatto WHERE id_museo = %s and epoca = %s"
            cursor.execute(query, (museo_richiesto, epoca_selezionata,))
            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                results.append(artefatto)
            cursor.close()
            cnx.close()
            return results

    @staticmethod
    def lettura_epoche():
        #Leggo tutte le epoche per popolare la dropdown
        results = []
        cnx= ConnessioneDB.get_connection()
        if cnx is None:
            print("Connessione Fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT DISTINCT epoca FROM artefatto"
            cursor.execute(query)
            for row in cursor:
                #artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                results.append(row["epoca"])
            cursor.close()
            cnx.close()
            return results



    # TODO