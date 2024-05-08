import networkx as nx
from database.DAO import DAO
class Model:
    def __init__(self):
        self._avg_distance = -1
        self.sol_graph = nx.Graph()
        self._airports = DAO.get_all_airports()
        self._airports_map = {}
        for a in self._airports:
            self._airports_map[a.id] = a

    def build_graph(self, avg_distance):
        # self.sol_graph.clear()
        # sel_flights = DAO.get_selected_flights(avg_distance)
        # for o1,d1,count_group1,avg_per_group1 in sel_flights:
        #     for o2,d2,count_group2,avg_per_group2 in sel_flights:
        #         if o1 == d2 and o2 == d1:
        #             if (avg_per_group1+avg_per_group2)/(count_group1+count_group2) > avg_distance:
        #                 self.sol_graph.add_edge(self._airports_map[o2],self._airports_map[d2])
        self.sol_graph.clear()
        sel_flights = DAO.get_selected_flights(avg_distance)
        for trip in sel_flights:
            #ERRORE NELLA MEDIA - non si calcola così
            trip_average = (trip[3] + trip[7]) / (trip[2] + trip[6])
            if trip_average > avg_distance:
                self.sol_graph.add_edge(self._airports_map[trip[0]],self._airports_map[trip[1]],weight = trip_average)



    def get_num_nodes(self):
        return len(self.sol_graph.nodes)

    def get_num_edges(self):
        return len(self.sol_graph.edges)



