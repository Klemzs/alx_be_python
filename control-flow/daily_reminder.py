task = input("Enter your task: ")
priority = input("Priority (high,medium,low): ")
time_bound = input("Is it time-bound (yes or no)? ")

match priority:
    case "high":
        if time_bound == "Yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
    case "low":
        if time_bound == "No":
            print(f"{task} is a low priority task. Consider completing it when you have free time")
    case _:
        print("Okay")
