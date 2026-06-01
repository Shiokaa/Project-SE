ifeq ($(OS),Windows_NT)
	PIP = .venv\Scripts\pip
	ACTIVATE_CMD = .\.venv\Scripts\Activate
	RM = rmdir /s /q .venv
else
	PIP = .venv/bin/pip
	ACTIVATE_CMD = source .venv/bin/activate
	RM = rm -rf .venv
endif

help:
	@echo "Available commands:"
	@echo "  make install    - Create virtual environment and install dependencies"
	@echo "  make activate   - Print the command to activate the virtual environment"
	@echo "  make uninstall  - Remove the virtual environment"

install:
	python3 -m venv .venv
	$(PIP) install -r requirements.txt

activate:
	@echo "$(ACTIVATE_CMD)"

uninstall:
	$(RM)
