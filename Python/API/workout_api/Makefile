run:
	@uvicorn web_api.main:app --reload

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)

run-migration:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head
