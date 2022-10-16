import time

from server.celery import app

from apps.endpoints.constants import StatusChoices


@app.task()
def predict_model(sleep_time, predict_progress_id):
    from apps.endpoints.models import PredictModelProcess
    # RUN you ML Process her if you need to make it async
    predict_model_process = PredictModelProcess.objects.get(id=predict_progress_id)
    try:
        time.sleep(int(sleep_time))
        predict_model_process.status = StatusChoices.DONE
        predict_model_process.response = {
            "message": "Success"
        }

    except:
        predict_model_process.status = StatusChoices.FAILED
        predict_model_process.response = {
            "message": "Failed"
        }
    predict_model_process.save()
