#========================================
# Scheduler Jobs
#========================================
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
scheduler = BackgroundScheduler()
scheduler.configure(timezone=utc)

# jobs
from example_apsschedulers import scheduler_jobs

scheduler.add_job(scheduler_jobs.FirstCronTest, 'interval', seconds=10)
scheduler.start()

#========================================