clean:
	rm -rf $(shell find . | grep pycache)

run: 
	python3 main.py