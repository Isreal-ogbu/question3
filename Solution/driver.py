import psycopg2.extras
import json
from bson import json_util 

# Connect to the database
conn = psycopg2.connect(
    host="host_name",
    database="database_name",
    user="username",
    password="user_password",
    cursor_factory=psycopg2.extras.DictCursor
)

# Create a cursor object
cur = conn.cursor()

# Execute a SELECT query
Query = "SELECT * FROM table_name"
cur.execute(Query)

# Fetch all the rows of the query result
rows = cur.fetchall()

data = {"status_code": 200, "data": rows}

# Convert the list of dictionaries to a JSON object
json_data = json.dumps(data, default=json_util.default)

# Print the JSON object
print(json_data)

# Close the cursor and the connection
cur.close()
conn.close()
