import datetime

# Define the time it takes for the average person to fall asleep
minutes_to_fall_asleep = 14

def calculate_wake_up_times(now):
    # Calculate the times the user should wake up, based on the current time
    wake_up_times = []
    for i in range(1, 7):
        wake_up_time = now + datetime.timedelta(minutes=(i*90 + minutes_to_fall_asleep))
        wake_up_times.append(wake_up_time.strftime("%-I:%M %p"))
    return wake_up_times

def calculate_bedtime(sleep_time):
    # Convert the sleep time string to a datetime object
    sleep_time = datetime.datetime.strptime(sleep_time, "%I:%M %p")
    
    # Calculate the times the user should wake up, based on the sleep time
    wake_up_times = []
    for i in range(1, 7):
        wake_up_time = sleep_time + datetime.timedelta(minutes=(i*90 + minutes_to_fall_asleep))
        wake_up_times.append(wake_up_time.strftime("%-I:%M %p"))
    return wake_up_times

def calculate_wake_up(sleep_time):
    # Convert the sleep time string to a datetime object
    wake_up_time = datetime.datetime.strptime(sleep_time, "%I:%M %p")
    
    # Calculate the times the user should get in bed, based on the wake up time
    bed_times = []
    for i in range(6, 0, -1):
        bed_time = wake_up_time - datetime.timedelta(minutes=(i*90 + minutes_to_fall_asleep))
        bed_times.append(bed_time.strftime("%-I:%M %p"))
    return bed_times

# Get the current time
now = datetime.datetime.now()

# User interface
print("Welcome to the Sleepyproject, which one do you want to choose?")
print("1) Going to bed now")
print("2) Pick a time to sleep")
print("3) Pick a time to wake up")

choice = input()
if choice == "1":
    wake_up_times = calculate_wake_up_times(now)
    print(f"It takes the average person {minutes_to_fall_asleep} minutes to fall asleep...")
    print("If you lie in bed now, try to wake up at one of the following times:")
    for i, time in enumerate(wake_up_times):
        print(f"{i+1} {time}")
elif choice == "2":
    sleep_time = input("Which time do you want to sleep? (hh:mm AM/PM) ")
    wake_up_times = calculate_bedtime(sleep_time)
    print(f"It takes the average person {minutes_to_fall_asleep} minutes to fall asleep...")
    print(f"If you lie in bed at {sleep_time}, try to wake up at one of the following times:")
    for i, time in enumerate(wake_up_times):
        print(f"{i+1} {time}")
elif choice == "3":
    wake_up_time = input("Which time do you want to wake up? (hh:mm AM/PM) ")
    bed_times = calculate_wake_up(wake_up_time)
    print(f"It takes the average person {minutes_to_fall_asleep} minutes to fall asleep...")
    print(f"If you wake up at {wake_up_time}, you should get in bed at one of the following times:")
    for i, time in enumerate(bed_times):
        print(f"{i+1} {time}")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")    