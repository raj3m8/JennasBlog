from django.shortcuts import render_to_response
import pymongo

def home(e):
	return render_to_response('index.html')

def dev(e):
	return render_to_response('home.html')
