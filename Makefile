PACKAGES=tutorial/ demo/

test: 
	@echo "===== TESTING ${PACKAGE} ====="
	pytest tests/

clean-pyc: 
	@echo "clean-pyc" 
	find . -name '*.pyc' -prune -exec rm -f {} \; 
	find . -name '__pycache__' -prune -exec rm -rf {} \; 
	find . -name '.pytype' -prune -exec rm -rf {} \; 
	find . -name '.mypy_cache' -prune -exec rm -rf {} \; 
	find . -name '.pytest_cache' -prune -exec rm -rf {} \; 
	find . -name '.scannerwork' -prune -exec rm -rf {} \; 
	find . -name '*.toc' -prune -exec rm -rf {} \;

lint:
	@echo "===== LINTING ${PACKAGE} ====="
	black -t py311 ${PACKAGE} demo/ tests/
	flake8 ${PACKAGE} tests/
	pylint ${PACKAGE} tests/
	mypy ${PACKAGE} tests/

all: lint test
