# city_graph.py
"""
A script drawing city graph.
"""
from typing import *

from graph import Graph
from weighted_graph import WeightedGraph


CITIES: list[str] = [
    "Seattle", "San Francisco", "Los Angeles",
    "Riverside", "Phoenix", "Chicago", "Boston", "New York",
    "Atlanta", "Miami", "Dallas", "Houston",
    "Detroit", "Philadelphia", "Washington"
]

# draw an unweighted graph of the cities
city_graph: Graph[str] = Graph(CITIES)
city_graph.add_edge_by_vertices("Seattle", "Chicago")
city_graph.add_edge_by_vertices("Seattle", "San Francisco")
city_graph.add_edge_by_vertices("San Francisco", "Riverside")
city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
city_graph.add_edge_by_vertices("Riverside", "Phoenix")
city_graph.add_edge_by_vertices("Riverside", "Chicago")
city_graph.add_edge_by_vertices("Phoenix", "Dallas")
city_graph.add_edge_by_vertices("Phoenix", "Houston")
city_graph.add_edge_by_vertices("Dallas", "Chicago")
city_graph.add_edge_by_vertices("Dallas", "Atlanta")
city_graph.add_edge_by_vertices("Dallas", "Houston")
city_graph.add_edge_by_vertices("Houston", "Atlanta")
city_graph.add_edge_by_vertices("Houston", "Miami")
city_graph.add_edge_by_vertices("Atlanta", "Chicago")
city_graph.add_edge_by_vertices("Atlanta", "Washington")
city_graph.add_edge_by_vertices("Atlanta", "Miami")
city_graph.add_edge_by_vertices("Miami", "Washington")
city_graph.add_edge_by_vertices("Chicago", "Detroit")
city_graph.add_edge_by_vertices("Detroit", "Boston")
city_graph.add_edge_by_vertices("Detroit", "Washington")
city_graph.add_edge_by_vertices("Detroit", "New York")
city_graph.add_edge_by_vertices("Boston", "New York")
city_graph.add_edge_by_vertices("New York", "Philadelphia")
city_graph.add_edge_by_vertices("Philadelphia", "Washington")

# draw a weighted graph of the cities
city_graph_weighted: WeightedGraph[str] = WeightedGraph(CITIES)
city_graph_weighted.add_edge_by_vertices("Seattle", "Chicago", 1737)
city_graph_weighted.add_edge_by_vertices("Seattle", "San Francisco", 678)
city_graph_weighted.add_edge_by_vertices("San Francisco", "Riverside", 386)
city_graph_weighted.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
city_graph_weighted.add_edge_by_vertices("Los Angeles", "Riverside", 50)
city_graph_weighted.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
city_graph_weighted.add_edge_by_vertices("Riverside", "Phoenix", 307)
city_graph_weighted.add_edge_by_vertices("Riverside", "Chicago", 1704)
city_graph_weighted.add_edge_by_vertices("Phoenix", "Dallas", 887)
city_graph_weighted.add_edge_by_vertices("Phoenix", "Houston", 1015)
city_graph_weighted.add_edge_by_vertices("Dallas", "Chicago", 805)
city_graph_weighted.add_edge_by_vertices("Dallas", "Atlanta", 721)
city_graph_weighted.add_edge_by_vertices("Dallas", "Houston", 225)
city_graph_weighted.add_edge_by_vertices("Houston", "Atlanta", 702)
city_graph_weighted.add_edge_by_vertices("Houston", "Miami", 968)
city_graph_weighted.add_edge_by_vertices("Atlanta", "Chicago", 588)
city_graph_weighted.add_edge_by_vertices("Atlanta", "Washington", 543)
city_graph_weighted.add_edge_by_vertices("Atlanta", "Miami", 604)
city_graph_weighted.add_edge_by_vertices("Miami", "Washington", 923)
city_graph_weighted.add_edge_by_vertices("Chicago", "Detroit", 238)
city_graph_weighted.add_edge_by_vertices("Detroit", "Boston", 613)
city_graph_weighted.add_edge_by_vertices("Detroit", "Washington", 396)
city_graph_weighted.add_edge_by_vertices("Detroit", "New York", 482)
city_graph_weighted.add_edge_by_vertices("Boston", "New York", 190)
city_graph_weighted.add_edge_by_vertices("New York", "Philadelphia", 81)
city_graph_weighted.add_edge_by_vertices("Philadelphia", "Washington", 123)


if __name__ == '__main__':
    
    import sys
    from pathlib import Path
    
    ch2_dir: Path = Path().absolute().parent / 'ch02_search_problems'
    sys.path.insert(0, ch2_dir)
    
    from rich import print
    
    from ch02_search_problems.generic_search import breadth_first_search, Node, node_to_path
    
    # find the shortest path between
    def reached_miami(city: str) -> bool:
        return city == 'Miami'
    
    shortest_path: Optional[Node[str]] = breadth_first_search(
        'Boston',
        reached_miami,
        city_graph.neighbors_for_vertex
    )
    if not shortest_path:
        print('No solution found using breadth-first search')
    else:
        path: list[str] = node_to_path(shortest_path)
        print('[b]Shortest path from Boston to Miami[/b]')
        print(path)