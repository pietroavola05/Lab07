from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()
        self._lista_musei = []
        self._lista_epoche = []


    def trova_museo(self, museo_richiesto):
        # Ritorna l'id del museo selezionato
        print("Trovando museo")
        # Estraiamo l'ID corretto dalla stringa del museo corretto
        #museo_richiesto è una stringa dove ogni campo è diviso da un "|"
        stringa_museo_richiesto = museo_richiesto.split("|")

        for museo in self._lista_musei: #lista id oggetti
            #museo.id è un intero dichiarato nel dto, quindi lo confronto cn un altro intero
            if museo.id == int(stringa_museo_richiesto[0]):
                # registro l'id del museo che ho trovato
                print("Cerco di memorizzare l'id del museo")
                return museo.id
            else:
                pass

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo_richiesto:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        print("Sono nel model")
        id_museo = self.trova_museo(museo_richiesto)
        print("Ho registrato l'id del museo", id_museo)
        lista_artefatti_filtrata = self._artefatto_dao.filtraggio_museo_epoca_artefatti(id_museo, epoca)
        return lista_artefatti_filtrata


    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        if len(self._lista_epoche) == 0:
            self._lista_epoche = self._artefatto_dao.lettura_epoche()
        else:
            print("Non è necessario leggere nuovamente le epoche")
        return self._lista_epoche

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        #Controllo se la mia lista è già popolata o la devo popolare
        if len(self._lista_musei) == 0:
            self._lista_musei = self._museo_dao.lettura_dabatase_museo()
        else:
            print("Non è necessario leggere nuovamente i dati dal museo")

        return self._lista_musei

        # TODO

