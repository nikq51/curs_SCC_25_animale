# Makefile pentru build & run Docker dostoievski App
# Se plasează în directorul rădăcină al repo-ului, după git clone

# Nume imagine și container
IMAGE_NAME     := animal_app
CONTAINER_NAME := animal_container
HOST_PORT      := 5011
CONT_PORT      := 5011

.PHONY: all build run stop clean

all: build run

# Construiește imaginea Docker din contextul curent (.)
build:
	docker build -t $(IMAGE_NAME) .

# Rulează containerul (oprește și șterge unul existent mai întâi)
run: stop
	docker run -d --name $(CONTAINER_NAME) -p $(HOST_PORT):$(CONT_PORT) $(IMAGE_NAME)
	@echo " Containerul '$(CONTAINER_NAME)' rulează pe http://127.0.0.1:$(HOST_PORT)/animal"

# Oprește și șterge containerul, dacă există
stop:
	-@docker stop $(CONTAINER_NAME) 2>/dev/null || true
	-@docker rm   $(CONTAINER_NAME) 2>/dev/null || true

# Curăță containerele (echivalent cu stop)
clean: stop
	@echo " Containerele oprite și șterse."
