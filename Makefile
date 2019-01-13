help:
	@echo 'Usage:                                         '
	@echo 'make start-api        start the api            '
	@echo 'make start-ui         start the ui             '
	@echo '                                               '

start-api:
	cd api && pipenv run vinyl/manage.py runserver

start-ui:
	cd ui && npm start
