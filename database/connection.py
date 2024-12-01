from py2neo import Graph

def get_db():
    # Connect to Neo4j database
    return Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))