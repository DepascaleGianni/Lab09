import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        avg_distance = self._view._txtIn.value
        if avg_distance == "":
            self._view.create_alert("write the avg distance")
            return

        self._model.build_graph(int(avg_distance))
        n_nodes = self._model.get_num_nodes()
        n_edges = self._model.get_num_edges()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {n_nodes} nodi."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {n_edges} archi"))
        self._view.update_page()

