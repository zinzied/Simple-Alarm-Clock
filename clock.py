import datetime
import time
import webbrowser
from playsound import playsound
import tkinter as tk
from tkinter import messagebox

alarm_times = []
alarm_active = False

def set_alarm():
    global alarm_active
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time in alarm_times:
            alarm_active = True
            while alarm_active:
                playsound('alarm_sound.mp3')  # Make sure you have an alarm sound file named 'alarm_sound.mp3'
        time.sleep(1)

def start_alarm():
    alarm_time = entry.get()
    if alarm_time:
        alarm_times.append(alarm_time)
        update_alarm_label()
    else:
        messagebox.showwarning("Input Error", "Please enter a valid time.")

def stop_alarm():
    global alarm_active
    alarm_active = False

def update_alarm_label():
    alarm_label.config(text="Alarms Set For: " + ", ".join(alarm_times))

def update_clock():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text="Current Time: " + current_time)
    root.after(1000, update_clock)  # Update the clock every second

def open_facebook():
    webbrowser.open("https://www.facebook.com/Ziedb1984")  # Replace with your Facebook profile URL

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")
root.configure(bg="#2E2E2E")  # Set background color

# Create and place the widgets
label = tk.Label(root, text="Enter the time to set the alarm (HH:MM:SS):", bg="#2E2E2E", fg="#FFFFFF", font=("Helvetica", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=5)

button = tk.Button(root, text="Set Alarm", command=start_alarm, bg="#4CAF50", fg="#FFFFFF", font=("Helvetica", 14))
button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Alarm", command=stop_alarm, bg="#F44336", fg="#FFFFFF", font=("Helvetica", 14))
stop_button.pack(pady=10)

clock_label = tk.Label(root, text="", font=("Helvetica", 48), bg="#2E2E2E", fg="#FFFFFF")  # Set a larger font size
clock_label.pack(pady=10)

alarm_label = tk.Label(root, text="", font=("Helvetica", 24), bg="#2E2E2E", fg="#FFFFFF")  # Label to show the set alarm times
alarm_label.pack(pady=10)

facebook_button = tk.Button(root, text="Visit my Facebook", command=open_facebook, bg="#3b5998", fg="#FFFFFF", font=("Helvetica", 14))
facebook_button.pack(pady=10)

# Start the clock update
update_clock()

# Start the alarm checking in a separate thread
import threading
alarm_thread = threading.Thread(target=set_alarm)
alarm_thread.daemon = True
alarm_thread.start()

# Run the application
root.mainloop()