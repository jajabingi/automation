import schedule
import time

def task_one():
    print("Task One is running!")

def task_two():
    print("Task Two is running!")

def stop_scheduler():
    print("Stopping the scheduler...")
    schedule.clear()
    # If you want to exit the script after stopping the scheduler, you can use sys.exit()
    # import sys
    # sys.exit()

# Schedule Task One every 2 seconds
schedule.every(2).seconds.do(task_one)

# Schedule Task Two every 5 seconds
schedule.every(5).seconds.do(task_two)

# Schedule to stop the scheduler after 20 seconds
schedule.every(20).seconds.do(stop_scheduler)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
