# Makefile pentru build & run Docker Alpaca App

# Nume subdirector proiect
PROJECT_DIR := curs_SCC_25_animale

# Nume imagine și container
IMAGE_NAME       := alpaca_app
CONTAINER_NAME   := alpaca_container
HOST_PORT        := 5000
CONTAINER_PORT   := 5000

.PHONY: all build run stop clean

all: build run

# Construiește imaginea Docker
build:
	docker build -t $(IMAGE_NAME) $(PROJECT_DIR)

# Rulează containerul (oprește și șterge unul existent mai întâi)
run: stop
	docker run -d --name $(CONTAINER_NAME) -p $(HOST_PORT):$(CONTAINER_PORT) $(IMAGE_NAME)
	@echo " Containerul '$(CONTAINER_NAME)' rulează pe http://localhost:$(HOST_PORT)/alpaca"

# Oprește și șterge containerul, dacă există
stop:
	-@docker stop $(CONTAINER_NAME) 2>/dev/null || true
	-@docker rm   $(CONTAINER_NAME) 2>/dev/null || true

# Curăță tot (echivalent cu stop)
clean: stop
	@echo " Containerele oprite și șterse."

