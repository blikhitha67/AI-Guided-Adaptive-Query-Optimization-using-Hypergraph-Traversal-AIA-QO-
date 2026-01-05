## Feature Engineering

In this project, feature engineering was performed to transform database and hypergraph information into input features for the AI-guided Adaptive Hypergraph Traversal (AHT) algorithm.

### 1. Node (Table) Features
For each table in the database, the following features were used:
- **Row count:** Number of rows in the table
- **Indexed columns:** Binary flags indicating whether key columns are indexed
- **Table size:** Storage size of the table (optional for AI input)

### 2. Hyperedge (Join) Features
For each multi-way join (hyperedge), the features included:
- **Tables involved:** List of tables connected by the hyperedge
- **Join type:** INNER, LEFT, RIGHT, FULL (encoded numerically)
- **Historical join cost:** Average execution time of the join from previous queries (used for training the AI)
- **Connectivity:** Number of adjacent hyperedges sharing tables
- **Number of tables in join:** Represents query complexity

### 3. Data Transformation
- **Normalization:** Row counts and historical join costs were normalized to ensure consistency in AI training.
- **Encoding:** Join types and index flags were converted to numerical values suitable for model input.
- **Hypergraph Representation:**  
  - Nodes correspond to tables with node features  
  - Hyperedges correspond to joins with hyperedge features  
- **AI Input:** The above features were fed to a predictive model to generate **priority scores** for each hyperedge.

### 4. Example Feature Representation
```text
Hyperedge E1:
- Tables: Customers, Orders, Shipments
- Row counts: [1000, 5000, 3000]
- Join type: INNER → 1 (numeric encoding)
- Indexed columns: [1,1,0]
- Historical cost: 120ms
- Connectivity: 2
- Number of tables in join: 3
