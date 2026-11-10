from werkzeug.security import generate_password_hash, check_password_hash

password = "secret123"  # pretend user just typed this

stored_hash = generate_password_hash(password)
print("Stored hash:", stored_hash)

print("Correct candidate check:",
      check_password_hash(stored_hash, "secret123"))

print("Wrong candidate check:",
      check_password_hash(stored_hash, "wrongpassword"))