from database.dao import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.nodes = []
        self.idMap = {}

    def costruisci_grafo(self, threshold):
        # 1. Pulizia grafo precedente
        self.G.clear()

        # 2. Aggiunta dei nodi (Hub)
        self.nodes = DAO.get_all_hubs()
        self.idMap = {h.id: h for h in self.nodes}  # Mappa id -> Oggetto Hub
        self.G.add_nodes_from(self.nodes)

        # 3. Aggiunta degli archi (filtrati per soglia)
        all_edges = DAO.get_all_connessioni()
        for u_id, v_id, peso in all_edges:
            if peso >= threshold:
                # Recupero gli oggetti Hub usando la mappa e creo l'arco
                nodo_u = self.idMap[u_id]
                nodo_v = self.idMap[v_id]
                self.G.add_edge(nodo_u, nodo_v, weight=peso)

    def get_num_nodes(self):
        return self.G.number_of_nodes()

    def get_num_edges(self):
        return self.G.number_of_edges()

    def get_all_edges(self):
        # Restituisce la lista degli archi con i relativi dati (peso)
        return list(self.G.edges(data=True))