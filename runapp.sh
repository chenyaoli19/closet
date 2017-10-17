#!/bin/bash
( cd ./client ; npm start ) & ( cd ./server/closetapp ; source bin/activate && python app.py) & (cd ~/site ; python -m SimpleHTTPServer 8000)

