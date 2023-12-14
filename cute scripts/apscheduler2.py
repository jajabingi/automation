from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def job_with_arguments(arg1, arg2):
    print(f"Job with arguments: {arg1}, {arg2}")

# Create a scheduler
scheduler = BlockingScheduler()

# Schedule a job using cron expression (every day at 2:30 PM)
scheduler.add_job(job_with_arguments, 'cron', hour=14, minute=30, args=['arg1_value', 'arg2_value'])

# Schedule a job to run once at a specific date and time
scheduler.add_job(job_with_arguments, 'date', run_date=datetime(2023, 1, 1, 12, 0, 0), args=['arg1_value', 'arg2_value'])

try:
    # Start the scheduler
    print("Scheduler started. Press Ctrl+C to exit.")
    scheduler.start()
except KeyboardInterrupt:
    # Handle Ctrl+C to gracefully shutdown the scheduler
    print("Scheduler stopped.")
