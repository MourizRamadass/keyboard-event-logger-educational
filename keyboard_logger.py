def log_key(key):
    print(f"Key Pressed: {key}")

print("Educational Keyboard Event Logger")
print("Type 'exit' to stop")

while True:
    key = input("Enter a key: ")

    if key.lower() == "exit":
        print("Logger Stopped")
        break

    log_key(key)
