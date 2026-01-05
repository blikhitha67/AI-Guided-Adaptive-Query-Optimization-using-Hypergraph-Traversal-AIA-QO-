# Results and Evaluation

## Experimental Setup

The **Adaptive Hypergraph Traversal (AHT)** algorithm was evaluated using a simulated relational database environment.  
The database consists of five tables:

- Customers  
- Orders  
- Products  
- Shipments  
- Suppliers  

Join relationships are modeled as a **hypergraph**, where:
- Nodes represent database tables
- Hyperedges represent multi-table joins

AI-predicted costs were simulated based on table statistics and historical execution behavior.

## Hypergraph Configuration

### Hyperedges

| Hyperedge | Tables Involved |
|----------|-----------------|
| E1 | Customers, Orders, Shipments |
| E2 | Orders, Products |
| E3 | Products, Suppliers |

### AI-Predicted Join Costs

| Hyperedge | Predicted Cost |
|----------|----------------|
| E1 | 95 |
| E2 | 70 |
| E3 | 80 |

Lower values indicate higher priority.

## Optimized Join Order

The optimized join order produced by the **Adaptive Hypergraph Traversal** algorithm is:
This ordering prioritizes lower-cost joins and delays expensive multi-table joins.

## Baseline Comparison

| Strategy | Join Order |
|--------|------------|
| Random Join Order | E1 → E2 → E3 |
| Static Cost-Based Sorting | E2 → E3 → E1 |
| **Adaptive Hypergraph Traversal (Proposed)** | **E2 → E3 → E1** |

Unlike static sorting, AHT dynamically adapts decisions based on hypergraph connectivity.

## Observations

- Low-cost joins are executed earlier
- Multi-table joins are deferred
- Shared table dependencies are handled adaptively
- Hypergraph modeling captures complex join relationships

## Key Results

- Successful integration of AI guidance with algorithmic traversal
- Reduced risk of expensive intermediate joins
- Scalable join planning using hypergraph structure
- Suitable for advanced DBMS research

## Limitations

- AI predictions are simulated
- No real query execution metrics
- Results reflect algorithmic behavior only

## Reproducibility

The results can be reproduced using:

- `adaptive_hypergraph_traversal.py`
- `feature_engineering.py`

Python version: **3.8+**
