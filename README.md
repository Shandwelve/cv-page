## A simple CV application

### Before start:
Create virtual environment:
```shell
python3 -m venv .venv
```
Activate venv:
```shell
source .venv/bin/activate
```
Install dependencies:
```shell
pip install -r requirements.txt
```
### Run application:
```shell
python3 -m flask run
```
### Application endpoints:
```shell
curl http://127.0.0.1:5000/personal
```
```shell
curl http://127.0.0.1:5000/experience
```
```shell
curl http://127.0.0.1:5000/education
```
```shell
curl http://127.0.0.1:5000/languages
```
### Application commands:
```shell
python3 -m flask print-cv-data
```