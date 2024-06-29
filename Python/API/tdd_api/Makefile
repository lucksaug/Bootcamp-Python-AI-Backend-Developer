run:
	@uvicorn store.main:app --reload

run-docker:
	@sudo docker-compose up -d

precommit-install:
	@pre-commit install

test:
	@pytest

test-matching:
	@pytest -s -rx -k $(K) --pdb store ./tests/
