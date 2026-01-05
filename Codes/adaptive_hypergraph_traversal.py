# adaptive_hypergraph_traversal.py

import heapq

class Hypergraph:
    def __init__(self):
        self.nodes = set()  # tables
        self.hyperedges = {}  # hyperedge_id -> list of connected nodes
        self.adjacency = {}  # node -> set of hyperedge_ids

    def add_node(self, node):
        self.nodes.add(node)
        if node not in self.adjacency:
            self.adjacency[node] = set()

    def add_hyperedge(self, edge_id, nodes):
        self.hyperedges[edge_id] = nodes
        for node in nodes:
            self.add_node(node)
            self.adjacency[node].add(edge_id)


def adaptive_hypergraph_traversal(H, ai_scores):
    """
    H: Hypergraph object
    ai_scores: dict of {hyperedge_id: predicted_score} from AI
    Returns: list of hyperedges in optimized join order
    """

    # Initialize priority queue
    pq = []
    for edge_id, nodes in H.hyperedges.items():
        score = ai_scores.get(edge_id, 1000)  # fallback score
        heapq.heappush(pq, (score, edge_id))

    join_order = []
    visited_edges = set()

    while pq:
        score, edge_id = heapq.heappop(pq)
        if edge_id in visited_edges:
            continue
        join_order.append(edge_id)
        visited_edges.add(edge_id)

        # Update scores of adjacent hyperedges
        for node in H.hyperedges[edge_id]:
            for adj_edge in H.adjacency[node]:
                if adj_edge not in visited_edges:
                    new_score = ai_scores.get(adj_edge, 1000)
                    heapq.heappush(pq, (new_score, adj_edge))

    return join_order


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    # Create hypergraph
    H = Hypergraph()
    H.add_hyperedge("E1", ["Customers", "Orders", "Shipments"])
    H.add_hyperedge("E2", ["Orders", "Products"])
    H.add_hyperedge("E3", ["Products", "Suppliers"])

    # Simulated AI predicted scores (lower = higher priority)
    ai_scores = {
        "E1": 95,
        "E2": 70,
        "E3": 80
    }

    optimized_order = adaptive_hypergraph_traversal(H, ai_scores)
    print("Optimized Join Order:", optimized_order)
