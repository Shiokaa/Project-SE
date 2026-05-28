ifeq ($(OS),Windows_NT)
	PIP = .venv\Scripts\pip
	ACTIVATE_CMD = .\.venv\Scripts\Activate
	RM = rmdir /s /q .venv
else
	PIP = .venv/bin/pip
	ACTIVATE_CMD = source .venv/bin/activate
	RM = rm -rf .venv
endif

install:
	python -m venv .venv
	$(PIP) install -r requirements.txt

activate:
	@echo "$(ACTIVATE_CMD)"

uninstall:
	$(RM)
