import tkinter as tk
from tkinter import messagebox
from functions import load_data, save_data, clock_in, clock_out, calculate_duration
import datetime

# Create the main application window
root = tk.Tk()
root.title("Timesheet Application")

data = load_data()

def clock_in_action():
    global data
    start_time = clock_in()
    data.append({'start': start_time.isoformat(), 'end': None})
    save_data(data)
    messagebox.showinfo("Clock In", f"Clocked in at {start_time}")
    update_timesheet()

def clock_out_action():
    global data
    if data and data[-1]['end'] is None:
        end_time = clock_out()
        start_time = datetime.datetime.fromisoformat(data[-1]['start'])
        duration = calculate_duration(start_time, end_time)
        data[-1]['end'] = end_time.isoformat()
        data[-1]['duration'] = str(duration)
        save_data(data)
        messagebox.showinfo("Clock Out", f"Clocked out at {end_time}\nSession duration: {duration}")
        update_timesheet()
    else:
        messagebox.showerror("Error", "No active session to clock out of.")

def show_timesheet():
    if not data:
        messagebox.showinfo("Timesheet", "No timesheet data available.")
    else:
        timesheet_entries = "\n".join([f"Start: {entry['start']}, End: {entry['end']}, Duration: {entry.get('duration', 'N/A')}" for entry in data])
        messagebox.showinfo("Timesheet", timesheet_entries)

def update_timesheet():
    timesheet_text.delete(1.0, tk.END)
    if not data:
        timesheet_text.insert(tk.END, "No timesheet data available.\n")
    else:
        for entry in data:
            start = entry['start']
            end = entry['end']
            duration = entry.get('duration', 'N/A')
            timesheet_text.insert(tk.END, f"Start: {start}, End: {end}, Duration: {duration}\n")

# Create buttons
clock_in_button = tk.Button(root, text="Clock In", command=clock_in_action)
clock_in_button.pack(pady=10)

clock_out_button = tk.Button(root, text="Clock Out", command=clock_out_action)
clock_out_button.pack(pady=10)

show_timesheet_button = tk.Button(root, text="Show Timesheet", command=show_timesheet)
show_timesheet_button.pack(pady=10)

# Create a text widget to display the timesheet
timesheet_text = tk.Text(root, height=10, width=50)
timesheet_text.pack(pady=10)
update_timesheet()

# Run the main event loop
root.mainloop()