import time

def countdown_timer(seconds):
    print(f"\nCountdown timer started for {seconds} seconds...\n")
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  
        time.sleep(1) 
        seconds -= 1

    print("\nTime's up! 🎉")
try:
    total_seconds = int(input("Enter the countdown time in seconds: "))
    if total_seconds > 0:
        countdown_timer(total_seconds)
    else:
        print("Please enter a positive number.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
