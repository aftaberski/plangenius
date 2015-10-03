from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from apps.events.forms import EventForm


def index(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        # import pdb
        # pdb.set_trace()
        event_form = EventForm(data=request.POST)

        # If the two forms are valid...
        if event_form.is_valid():
            # Save the user's form data to the database.
            event = event_form.save(commit=False)
            if request.user.is_authenticated():
              event.organizer = request.user

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.

            event.save()
            return HttpResponseRedirect('/')
            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print event_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        event_form = EventForm()

    # Render the template depending on the context.
    return render_to_response(
            'events/event_form.html',
            {'event_form': event_form, 'registered': registered},
            context)