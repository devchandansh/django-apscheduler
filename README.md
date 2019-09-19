# django-apscheduler
Django APScheduler for Scheduler Jobs. Advanced Python Scheduler (APScheduler) is a Python library that lets you schedule your Python code to be executed later, either just once or periodically. You can add new jobs or remove old ones on the fly as you please. 



## Installing APScheduler
* install apscheduler 
```
pip install apscheduler
```




## Configuring the scheduler
make execute.py file and add the below codes


```
from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
```



* Your written functions

```
from schedulejobs import views 

scheduler.add_job(views.FirstCronTest, 'interval', seconds=10)
scheduler.start()

```



## Link the File for Execution 
Now, add the below line in the bottom of Url file

```
from example_apsschedulers import execute
```




## References:
* https://apscheduler.readthedocs.io/en/3.0/userguide.html




