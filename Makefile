.PHONY: dev
dev:
	fswatch -o main.py | xargs -n1 -I{} python main.py

