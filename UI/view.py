import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def mostra_artefatti_clicked(self, e):
        # quando clicco su mostra artefatti richiamo la funzione del controller
        self.controller.filtraggio_per_selezione()

    def load_interface(self):
        # crea tutti gli elementi dell’interfaccia e li aggiunge alla pagina
        # --- sezione 1: intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- sezione 2: filtraggio ---
        # qua devo creare i miei due dropdown (uno per i musei e uno per gli artefatti)
        self._dropdown_musei = ft.Dropdown(label="Musei")
        self._dropdown_artefatti = ft.Dropdown(label="Artefatti")

        # chiamo il controller per riempire i dropdown con i dati
        self.controller.popola_dropdown()

        # --- sezione 3: artefatti ---
        # qui creo il pulsante che mostra gli artefatti e la lista dove li metto
        self.pulsante_mostra_artefatti = ft.ElevatedButton("Mostra Artefatti", on_click=self.mostra_artefatti_clicked)
        self._lista_finale = ft.ListView(expand=True, spacing=10, padding=20)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(spacing = 50,
                   controls=[self._dropdown_musei, self._dropdown_artefatti],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),
            # TODO

            # Sezione 3: Artefatti
            ft.Row(spacing = 50,
                   controls=[self.pulsante_mostra_artefatti],
                   alignment=ft.MainAxisAlignment.CENTER),
            self._lista_finale,
            # TODO
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
