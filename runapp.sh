#!/bin/bash
( cd ./client ; npm start ) & ( cd ./server/closetapp ; source bin/activate && python app.py)

