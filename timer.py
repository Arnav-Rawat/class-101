import time
def countdown_timer(seconds):
    while seconds > 0 :
        mins = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{mins}:{secs}'
        print(timer)
        seconds -=1
    print("Time up!")

seconds = input("Enter time no. in seconds")
countdown_timer(int(seconds))    