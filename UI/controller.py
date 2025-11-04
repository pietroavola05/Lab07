import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        lista_musei = self._model.get_musei()
        lista_epoche = self._model.get_epoche()
        for elemento in lista_musei:
            self._view._dropdown_musei.options.append(ft.dropdown.Option(elemento))
        for elemento in lista_epoche:
            self._view._dropdown_artefatti.options.append(ft.dropdown.Option(elemento))
    # TODO


    # CALLBACKS DROPDOWN
    def filtraggio_per_selezione(self):
        self.museo_selezionato = self._view._dropdown_musei.value
        self.epoca_selezionata = self._view._dropdown_artefatti.value

        #svuota la lista prima di ogni nuovo filtro
        self._view._lista_finale.controls.clear()

        if self.museo_selezionato is None or self.epoca_selezionata is None:
            self._view.show_alert("Seleziona prima un museo e un epoca")
        else:
            print("Sono nell'else")

            #trova l'ID del museo e ottieni la lista filtrata
            artefatti_filtratti = self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)

            print("Sto facendo il for per aggiungere alla lista finale della view dopo aver ricevuto i miei dati")

            if artefatti_filtratti:
                for elemento in artefatti_filtratti:
                    # usiamo str(elemento) per visualizzare il risultato del __str__ del DTO
                    self._view._lista_finale.controls.append(ft.Text(str(elemento)))
            else:
                self._view._lista_finale.controls.append(
                    ft.Text("Nessun artefatto trovato per i filtri selezionati."))

        self._view.update()  # l'update finale presente nella view come funzione



    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
