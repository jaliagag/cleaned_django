FROM python:3.12-rc-alpine3.16
RUN apk update && apk upgrade
WORKDIR Proyecto1/
CMD [ "python", "manage.py runserver" ]
