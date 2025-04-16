# obtencion_datos_mercado/jobs.py
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django_apscheduler.models import DjangoJobExecution
from .views import extraer_ofertas_tecnoempleo, extraer_ofertas_infojobs, extraer_ofertas_linkedin, extraer_ofertas

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(extraer_ofertas_tecnoempleo, 'interval', hours=1, replace_existing=True, id='tecnoempleo', jobstore='default')
    scheduler.add_job(extraer_ofertas_infojobs, 'interval', hours=1, replace_existing=True, id='infojobs', jobstore='default')
    scheduler.add_job(extraer_ofertas_linkedin, 'interval', hours=1, replace_existing=True, id='linkedin', jobstore='default')
    scheduler.add_job(extraer_ofertas, 'interval', hours=1, replace_existing=True, id='infojobs2', jobstore='default')
    register_events(scheduler)
    scheduler.start()