from apscheduler.schedulers.blocking import BlockingScheduler

def my_job():
    print("Job is running!")

# Create a scheduler
scheduler = BlockingScheduler()

# Schedule the job to run every 5 seconds
scheduler.add_job(my_job, 'interval', seconds=5)

try:
    # Start the scheduler
    print("Scheduler started. Press Ctrl+C to exit.")
    scheduler.start()
except KeyboardInterrupt:
    # Handle Ctrl+C to gracefully shutdown the scheduler
    print("Scheduler stopped.")
