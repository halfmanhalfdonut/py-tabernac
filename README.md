# Bible API

## Install
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

## Running (Dev)
1. `FLASK_APP=tabernac TABERNAC_DB=/path/to/file.db flask run`

## Running (Prod)
1. `TABERNAC_DB=/path/to/file.db gunicorn tabernac:app -b 127.0.0.1:{PORT} -D --pid tabernac-py-pid.txt`