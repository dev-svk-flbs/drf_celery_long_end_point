# Deploy Machine Learning Models with Django

This is a source code from the tutorial available at [deploymachinelearning.com](https://deploymachinelearning.com)

This web service makes Machine Learning models available with REST API. It is different from most of the tutorials available on the internet:

- it keeps information about many ML models in the web service. There can be several ML models available at the same endpoint with different versions. What is more, there can be many endpoint addresses defined.
- it stores information about requests sent to the ML models, this can be used later for model testing and audit.
- it has tests for ML code and server code,
- it can run A/B tests between different versions of ML models.

## The code structure

In the `research` directory there are:

- code for training machine learning models on Adult-Income dataset [link](https://github.com/pplonski/my_ml_service/blob/master/research/train_income_classifier.ipynb)
- code for simulating A/B tests [link](https://github.com/pplonski/my_ml_service/blob/master/research/ab_test.ipynb)

In the `backend` directory there is Django application.

In the `docker` directory there are dockerfiles for running the service in the container.


## Django + React Tutorial :books:

I'm working on complete tutorial how to build SaaS (software as a Service) application with Django and React from scratch. The SaaS service will be for server uptime monitoring - it is available at [monitor-uptime.com](https://monitor-uptime.com). The tutorial is available at [SaaSitive website](https://saasitive.com/react-django-tutorial/).


## Setting Up Project for Local Env

### Django Project Setup

1. Install Requirements
```pip install -r requirements.txt```
2. Setup redis if not present on system. https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-22-04
3. Open terminal activate virtual environment.
4. Start django server by `python manage.py runserver`.
5. Open another terminal.
6. Start celery server by `celery -A server worker -l info`.
7. Now call the api as per need.