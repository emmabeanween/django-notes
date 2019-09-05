

from django.shortcuts import render 
from django.http import HttpResponse
from notes.forms import LoginForm, RegisterForm, NoteForm
from notes.settings import STATIC_URL
from django.contrib import messages
from notes.models import User, Note
import string
import datetime
import random
from random import randint
from django.shortcuts import redirect
from django.template.context import RequestContext



def myLogin(request):
	if request.method == "POST":
		filledForm = LoginForm(request.POST)
		if filledForm.is_valid():
			username = filledForm.cleaned_data['username']
			password = filledForm.cleaned_data['password']
			#check that username and password are valid
			user_exists = User.objects.filter(username = username, password=password ).all()
			if len(user_exists) == 0:
				messages.add_message(request, messages.INFO, 'Your username and/or password are incorrect.')
				return render(request, "login.html", {'form': filledForm})
			else:
				request.session['username'] = username
				return redirect("myHome")
			
	return render(request, "login.html", {'form': LoginForm()})



def myRegister(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			registererrors = []
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			username_already_exists = User.objects.filter(username = username).all()
			if len(username_already_exists) > 0:
				registererrors.append("That username is already taken.")
			if len (str(username)) < 6 or len(str(password)) < 6:
				registererrors.append("Username and password must both be at least six characters.")
			if registererrors:
				for error in registererrors:
					messages.add_message(request, messages.INFO, error)
					return render(request, "register.html", {'form': form})
			else:
				#add new user
				random_id = randint(100000, 999999) 
				new_user = User(username = username, password=password, user_id = random_id)
				new_user.save()
				#start session with new user info and log them in
				messages.add_message(request, messages.INFO, "Congrats! You're now a new user. Add a new note under 'new note' above.")
				request.session['username'] = username  
				return redirect("myHome")

	return render(request, "register.html", {'form': RegisterForm()})


def myHome(request):
	if 'username' not in request.session:
		return redirect("myLogin")
	if request.method == "POST":
		#delete the account
		user_in_session = request.session['username']
		user_to_delete = User.objects.filter(username=user_in_session).first()
		user_to_delete.delete()
		request.session.flush()
		return redirect("myLogin")
	return render(request, "home.html", {'notes': Note.objects.filter(user_created = request.session['username']).all(), 
		'username': request.session['username'], 'form': NoteForm()})


def newNote(request):
	if 'username' not in request.session:
		return redirect("myLogin")
	if request.method == "POST":
		#obtain title and content
		title = request.POST.get("title")
		content = request.POST.get("content")
		user_made = request.session['username']
		random_id = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
		note = Note(title = title, content=content, note_id = random_id, user_created=user_made)
		note.save()
		messages.add_message(request, messages.INFO, "New note added.")
		return redirect("myHome")

	return render(request, "newnote.html", {'username': request.session['username'], 'form': NoteForm()})


def viewNote(request, id):
	if 'username' not in request.session:
		return redirect("myLogin")
	viewed_note = Note.objects.filter(note_id = id).first()
	if request.method == "POST":
		if 'save' in request.POST:
			#update/save the note
			new_title = request.POST.get("title")
			new_content = request.POST.get("content")
			viewed_note.title = new_title
			viewed_note.content = new_content
			viewed_note.date_added = datetime.datetime.now()
			viewed_note.save()
			messages.add_message(request, messages.INFO, "Note saved.")
			return redirect("myHome")

		else:
			#delete the note
			viewed_note.delete()
			messages.add_message(request, messages.INFO, "Note deleted.")
			return redirect("myHome")

	return render(request, "viewnote.html", {'username': request.session['username'], 'note': viewed_note, 'form': NoteForm()})

def leave(request):
	request.session.flush()
	return redirect("myLogin")

