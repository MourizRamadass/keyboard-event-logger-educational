# keyboard-event-logger-educational
#Keyboard Event Logger

## Description
This project demonstrates how keyboard events can be processed in a safe and controlled environment.

## Features
- Simulates key press logging
- Does not capture real keyboard input
- Educational demonstration only

## Run

```bash
python keyboard_logger.py
```

## Task Screenshot

![Task Screenshot](screenshot.png)
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
