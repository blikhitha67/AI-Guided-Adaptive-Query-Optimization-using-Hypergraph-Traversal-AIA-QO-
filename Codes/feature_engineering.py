# feature_engineering.py

import pandas as pd

# Simulated table statistics
tables = {
    "Customers": {"rows": 1000, "indexed": True, "size": 10},
    "Orders": {"rows": 5000, "indexed": True, "size": 50},
    "Products": {"rows": 2000, "indexed": False, "size": 20},
    "Shipments": {"rows": 3000, "indexed": False, "size": 15},
    "Suppliers": {"rows": 500, "indexed": True, "size": 5}
}

# Simulated hyperedges
hyperedges = {
    "E1": ["Customers", "Orders", "Shipments"],
    "E2": ["Orders", "Products"],
    "E3": ["Products", "Suppliers"]
}

# Create features dataframe
features = []
for edge_id, tables_in_edge in hyperedges.items():
    edge_feature = {
        "hyperedge": edge_id,
        "num_tables": len(tables_in_edge),
        "connectivity": sum([len(tables_in_edge) for t in tables_in_edge]),  # simplified
        "historical_cost": 100  # placeholder, can simulate AI input
    }
    for t in tables_in_edge:
        edge_feature[f"{t}_rows"] = tables[t]["rows"]
        edge_feature[f"{t}_indexed"] = int(tables[t]["indexed"])
    features.append(edge_feature)

df_features = pd.DataFrame(features)
print("Feature Engineering Output:\n", df_features)
