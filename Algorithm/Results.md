## Results – Adaptive Hypergraph Traversal (AHT)

The Adaptive Hypergraph Traversal algorithm was tested on a sample hypergraph representing database tables and multi-way joins.

### Sample Hypergraph
- **Nodes (Tables):** Customers, Orders, Products, Shipments, Suppliers
- **Hyperedges (Joins):**
  - E1: Customers, Orders, Shipments
  - E2: Orders, Products
  - E3: Products, Suppliers

### AI-Predicted Scores (Lower = Higher Priority)
| Hyperedge | AI Score |
|-----------|----------|
| E1        | 95       |
| E2        | 70       |
| E3        | 80       |

### Optimized Join Order (Output of AHT)
