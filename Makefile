all: run

run:
	uv run main.py

clean:
	rm -fr .venv/