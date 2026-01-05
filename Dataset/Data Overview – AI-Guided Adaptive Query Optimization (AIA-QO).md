# Data Overview – AI-Guided Adaptive Query Optimization (AIA-QO)

## Structural Representation

The relational database is modeled as a **hypergraph**:

- **Nodes:** Represent database tables.
- **Hyperedges:** Represent multi-way joins connecting two or more tables.

> Hypergraphs capture complex relationships between tables efficiently, especially for multi-table joins, which are common in DBMS and advanced analytics.


## Feature Representation for AI

Each hyperedge has features used by the AI module to predict traversal priorities:

- **Table statistics:** row counts, column cardinalities, table sizes
- **Join metadata:** type of join (INNER, LEFT, RIGHT, FULL), index presence
- **Historical performance:** past execution cost or runtime
- **Connectivity:** number of adjacent hyperedges sharing nodes
- **Query complexity:** number of tables involved

> The AI model outputs a **predicted score** for each hyperedge, indicating its priority in traversal.


## Interaction Between Data, AI, and DSA

The data serves as a **bridge between AI and DSA**:

1. **Structural role:** Defines the hypergraph representing the search space for joins.
2. **Informational role:** Provides statistics for scoring hyperedges.
3. **Predictive role:** Feeds AI predictions that guide the **Adaptive Hypergraph Traversal (AHT)** algorithm.

The AHT algorithm dynamically selects hyperedges based on **predicted cost and priority**, producing an optimized join order.

## Theoretical Advantages

- **Scalability:** Hypergraphs efficiently model multi-way joins.
- **Adaptability:** AI predictions enable dynamic adjustments for changing workloads.
- **Efficiency:** Priority-based traversal reduces computational overhead and avoids high-cost intermediate results.
- **Domain Relevance:** Applicable to **DBMS query optimization** and advanced analytics.


## Datasets

- **Synthetic Queries:** Generate tables and multi-way joins with simulated statistics for testing.
- **Benchmark Datasets:** Standard datasets such as **TPC-H** and **TPC-DS**.
- **Optional Real-World Logs:** Historical query execution logs from relational databases.


## Summary

In AIA-QO, data is **multi-layered**:

- **Structural knowledge:** Hypergraph representing tables and joins
- **Quantitative metrics:** Features for AI predictions
- **Dynamic guidance:** AI scores guiding algorithm traversal
