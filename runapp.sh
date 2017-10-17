#!/bin/bash
( cd ./client update ; npm start ) & ( cd ./server/closetapp ; source bin/activate && python app.py)

