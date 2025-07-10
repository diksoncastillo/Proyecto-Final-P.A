import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('SELECT id, username, password FROM users')
usuarios = cursor.fetchall()

print("Usuarios registrados:")
for u in usuarios:
    print(f"ID: {u[0]}, Usuario: {u[1]}, Contraseña hash: {u[2]}")

conn.close()
