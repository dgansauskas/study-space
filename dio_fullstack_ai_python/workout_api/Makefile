run:
	@echo "Iniciando serviços com Docker Compose..."
	@docker-compose up -d
	@echo "Iniciando a aplicação com Uvicorn..."
	@uvicorn workout_api.main:app --reload

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head