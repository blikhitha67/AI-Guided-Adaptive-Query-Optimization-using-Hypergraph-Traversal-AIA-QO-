## Custom Algorithm – Adaptive Hypergraph Traversal (AHT)

The **Adaptive Hypergraph Traversal (AHT)** algorithm is a novel algorithm developed as part of this project. It combines **AI-guided predictions** with **graph traversal techniques** to optimize multi-way joins in a database.  

### Algorithm Concept

1. Represent the database as a **hypergraph**:
   - **Nodes:** Tables  
   - **Hyperedges:** Multi-way joins  
2. Each hyperedge is assigned a **predicted score** from the AI model, representing its **priority** for traversal.  
3. The algorithm dynamically selects hyperedges with the **lowest predicted cost**, while considering **connectivity and query complexity**, to generate an **optimized join order**.  
4. Lookahead and priority updates ensure that **high-cost intermediate results are avoided**.

---

### Pseudo-code

```text
Input: 
    H = (Tables, Hyperedges)  // Hypergraph representation
    P = AI predictions for each hyperedge
Output: 
    join_order = Optimized join order for query execution

1. Initialize empty list join_order
2. Initialize priority queue Q

3. For each hyperedge e in H:
       Compute score: 
           score(e) = heuristic(e) + P[e]
       Insert (score(e), e) into Q

4. While Q is not empty:
       Pop hyperedge e with lowest score from Q
       Add e to join_order

       For each adjacent hyperedge e_adj not in join_order:
           Update score:
               score(e_adj) = heuristic(e_adj) + P[e_adj]
           If e_adj is already in Q:
               Update its priority
           Else:
               Insert e_adj into Q

       Optionally, apply lookahead or pruning to avoid high-cost intermediate joins

5. Return join_order
