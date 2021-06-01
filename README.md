# Requirements
Python 3.8

# Installation
source venv/bin/activate
pip install -r requirements.txt

# Run App
python app.py

# Run tests:
python -m pytest --cov-config=/home/walterschweitzer/projects/wayfair/.coveragec --cov=. tests/

# Run test HTML coverage report:
python -m pytest --cov-config=/home/walterschweitzer/projects/wayfair/.coveragec --cov=. tests/ --cov-report term-missing --cov-report html:cov_html