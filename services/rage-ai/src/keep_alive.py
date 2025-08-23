import time
import datetime

def main():
    print("Starting python rage-ai service...")
    while True:
        timestamp = datetime.datetime.now().isoformat()
        print(f"python rage-ai alive {timestamp}")
        time.sleep(60)

if __name__ == "__main__":
    main()