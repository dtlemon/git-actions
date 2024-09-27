all:

clean:
	rm -rf __pycache__
	rm -rf webapp/__pycache__
	rm -rf tests/__pycache__
	
test:
	pytest

run:
	flask --app webapp/app.py run
