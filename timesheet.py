import datetime  # Import datetime module
from functions import load_data, save_data, clock_in, clock_out, calculate_duration

def main():
    data = load_data()
    while True:
        print("\nTimesheet Menu")
        print("1. Clock In")
        print("2. Clock Out")
        print("3. Show Timesheet")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        print(f"User selected option: {choice}")  # Debugging statement

        if choice == '1':
            start_time = clock_in()
            print(f"Clocked in at {start_time}")
            data.append({'start': start_time.isoformat(), 'end': None})
            save_data(data)
        elif choice == '2':
            if data and data[-1]['end'] is None:
                end_time = clock_out()
                start_time = datetime.datetime.fromisoformat(data[-1]['start'])
                duration = calculate_duration(start_time, end_time)
                data[-1]['end'] = end_time.isoformat()
                data[-1]['duration'] = str(duration)
                save_data(data)
                print(f"Clocked out at {end_time}")
                print(f"Session duration: {duration}")
            else:
                print("No active session to clock out of.")
        elif choice == '3':
            if not data:
                print("No timesheet data available.")
            else:
                print("\nTimesheet Entries:")
                for entry in data:
                    start = entry['start']
                    end = entry['end']
                    duration = entry.get('duration', 'N/A')
                    print(f"Start: {start}, End: {end}, Duration: {duration}")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()