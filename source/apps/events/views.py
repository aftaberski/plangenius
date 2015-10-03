from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from apps.events.forms import EventForm


def index(request):

    context = RequestContext(request)

    registered = False

    if request.method == 'POST':

        event_form = EventForm(data=request.POST)

        if event_form.is_valid():

            event = event_form.save(commit=False)
            if request.user.is_authenticated():
              event.organizer = request.user


            event.save()
            return HttpResponseRedirect('/')

            registered = True

        else:
            print event_form.errors

    else:
        event_form = EventForm()

    return render_to_response(
            'events/event_form.html',
            {'event_form': event_form, 'registered': registered},
            context)