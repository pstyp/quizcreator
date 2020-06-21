#! /bin/bash
cd /home/jenkins/project/quizcreator
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
venv/bin/gunicorn --workers=4 --bind=0.0.0.0:5000 app:app
