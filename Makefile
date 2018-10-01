test:
	docker build . -t kata && docker run --rm -ti kata
