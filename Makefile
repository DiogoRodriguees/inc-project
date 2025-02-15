default:
	@python ./src/main.py
# @echo "no command default"

run:
	python main.py

install-dependencies:
	pip install -r requirements.txt