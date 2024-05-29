FROM python:3.12

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} ./Makefile Makefile
COPY --chown=${USER} ./manage.py manage.py
COPY --chown=${USER} ./django_csv_analysis django_csv_analysis
COPY --chown=${USER} ./core core
COPY --chown=${USER} ./.env.example .env
COPY --chown=${USER} ./templates /wd/templates
COPY --chown=${USER} ./media /wd/media

USER ${USER}
