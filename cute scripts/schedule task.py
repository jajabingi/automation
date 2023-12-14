import schedule
import time

def my_task():
    print("Task is running!")

# Schedule the task to run every minute
schedule.every(1).minutes.do(my_task)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
