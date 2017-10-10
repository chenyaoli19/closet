#!/usr/bin/env python
from __future__ import print_function
import mysql.connector
import os  

WEB_HOST = 'http://localhost:8000/closet/'

def db_connect():
	cnx = mysql.connector.connect(user='root', password='***', database='closet')
	cursor = cnx.cursor()
	return cnx, cursor

def load_image_to_DB(cnx, cursor):
	image_list = get_image_file_list()

	for image in image_list:
		image_url = WEB_HOST+image

		add_item = ("INSERT INTO items "\
			   		"(image_url) "\
			   		"VALUES ('%s')") % image_url
		cursor.execute(add_item)
		cnx.commit()

	cursor.close()
	cnx.close()

def get_image_file_list():
	image_list = []
	for image_file in os.listdir('./closet/'):
		image_list.append(image_file)
	return image_list

if __name__ == '__main__':
	#connect to db, return cnx and cursor
	cnx, cursor = db_connect()
	# connect to webserver
	load_image_to_DB(cnx, cursor)
	print('script executed.')
