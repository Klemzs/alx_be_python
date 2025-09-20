task = input("Enter a task description: ")
priority = input("What is the task priority (high,medium,low): ")
time_bound = input("Is task time-bound (Yes or No)? ")

match priority:
    case "high":
        if time_bound == "Yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
    case "low":
        if time_bound == "No":
            print(f"{task} is a low priority task. Consider completing it when you have free time")
    case _:
        print("Okay")
