from database.connection import get_db

db = get_db()

def create_user(username, name, age):
    query = """
    CREATE (u:User {username: $username, name: $name, age: $age})
    """
    db.run(query, username=username, name=name, age=int(age))

def connect_users(user1, user2):
    query = """
    MATCH (u1:User {username: $user1}), (u2:User {username: $user2})
    MERGE (u1)-[:FRIENDS_WITH]->(u2)
    """
    db.run(query, user1=user1, user2=user2)

def get_recommendations(username):
    query = """
    MATCH (u:User {username: $username})-[:FRIENDS_WITH]->(f)-[:FRIENDS_WITH]->(fof)
    WHERE NOT (u)-[:FRIENDS_WITH]->(fof) AND u <> fof
    RETURN fof.username AS recommended
    """
    result = db.run(query, username=username)
    return [record["recommended"] for record in result]