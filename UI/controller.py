import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        # 1. Recupero e validazione input
        try:
            soglia = float(self._view.guadagno_medio_minimo.value)
        except ValueError:
            self._view.show_alert("Inserire un valore numerico valido!")
            return

        # 2. Creazione del grafo
        self._model.costruisci_grafo(soglia)

        # 3. Aggiornamento output
        self._view.lista_visualizzazione.controls.clear()

        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Hubs: {self._model.get_num_nodes()}")
        )
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Tratte: {self._model.get_num_edges()}")
        )

        # Stampa delle tratte
        # u e v sono oggetti Hub, quindi verranno stampati usando il loro __str__ (Nome (Stato))
        all_edges = self._model.get_all_edges()
        for u, v, data in all_edges:
            self._view.lista_visualizzazione.controls.append(
                ft.Text(f"{u} -> {v} -- guadagno Medio Per Spedizione: € {data['weight']:.2f}")
            )

        self._view.update()