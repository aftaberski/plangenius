from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from apps.events.forms import EventForm
from .models import Event


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
            event_form.save_m2m()
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


def event_detail(request, event_slug):
  context_dict = {}
  try:
    print "***** made it here *****"
    event = Event.objects.get(slug=event_slug)

    context_dict['event'] = event

    # Added in order to add page to category

  except Event.DoesNotExist:
    pass

  return render(request, 'events/event_detail.html', context_dict)


def meal_category(request, event_slug):
  context_dict = {}
  try:
    print "***** made it here *****"
    event = Event.objects.get(slug=event_slug)

    context_dict['event'] = event
    context_dict['items'] = event.voting_options.filter(category="Meal")
    context_dict['type'] = 'Meals'
    # Added in order to add page to category

  except Event.DoesNotExist:
    pass

  return render(request, 'events/item_index.html', context_dict)

def activity_category(request, event_slug):
  context_dict = {}
  try:
    event = Event.objects.get(slug=event_slug)

    context_dict['event'] = event
    context_dict['items'] = event.voting_options.filter(category="Activities")
    context_dict['type'] = 'Activity'
    # Added in order to add page to category

  except Event.DoesNotExist:
    pass

  return render(request, 'events/item_index.html', context_dict)

def accommodation_category(request, event_slug):
  context_dict = {}
  try:
    event = Event.objects.get(slug=event_slug)

    context_dict['event'] = event
    context_dict['items'] = event.voting_options.filter(category="Accommodation")
    context_dict['type'] = 'Accommodations'
    # Added in order to add page to category

  except Event.DoesNotExist:
    pass

  return render(request, 'events/item_index.html', context_dict)