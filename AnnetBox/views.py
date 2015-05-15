# -*- coding: UTF-8 -*-
from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response
from django.template import RequestContext
import django
from annet.settings import MEDIA_URL, STATIC_URL
from AnnetBox.models import *


def login(request):
    return render_to_response("login.html", context_instance=RequestContext(request))


def main(request):
    """Main listing."""
    images = Image.objects.all()
    slides = Slide.objects.all()
    short_by_me = TextBlock.objects.filter(tag__name__contains='short_by_me')
    contacts = Personal.objects.all()[0]
    type_works = TypeWork.objects.all()
    tickets = Ticket.objects.filter(status__name='Открыта')
    if 'username' in request.POST.keys() and 'password' in request.POST.keys():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django.contrib.auth.login(request, user)
    if 'name' in request.POST.keys() and 'mobile' in request.POST.keys():
        name = request.POST['name']
        mobile = request.POST['mobile']
        if name != '' and mobile != '':
            secname = request.POST['secname']
            email = request.POST['email']
            type_work = request.POST['type_work']
            date = request.POST['date']
            time = request.POST['time']
            desc = request.POST['message']
            if time == '':
                time = None
            if date == '':
                date = None
            if TicketStatus.objects.filter(name="Открыта").exists():
                status = TicketStatus.objects.get(name="Открыта")
            else:
                status = TicketStatus.objects.create(name="Открыта")
            ticket = Ticket(first_name=name, last_name=secname, email=email, phone=mobile,
                            type_work=TypeWork.objects.get(type_work=type_work), date=date,
                            time=time, description=desc, viewed=False, status=status)
            ticket.save()
            tickets = Ticket.objects.filter(status__name='Открыта')
            return render_to_response("home.html",
                                      dict(tickets=tickets, images=images, type_works=type_works, contacts=contacts,
                                           slides=slides,
                                           short_by_me=short_by_me, user=request.user,
                                           media_url=MEDIA_URL, static_url=STATIC_URL),
                                      context_instance=RequestContext(request))

    return render_to_response("home.html",
                              dict(tickets=tickets, images=images, type_works=type_works, contacts=contacts,
                                   slides=slides,
                                   short_by_me=short_by_me, user=request.user,
                                   media_url=MEDIA_URL, static_url=STATIC_URL),
                              context_instance=RequestContext(request))


def services(request):
    """services listing."""
    type_works = TypeWork.objects.all()
    provide_services = TextBlock.objects.filter(tag__name__contains='provide_service')

    return render_to_response("services.html",
                              dict(type_works=type_works, provide_services=provide_services, user=request.user,
                                   media_url=MEDIA_URL, static_url=STATIC_URL))


def about(request):
    """about listing."""
    personal = Personal.objects.all()[0]
    about = TextBlock.objects.filter(tag__name__contains='about')
    awards = Award.objects.all()

    return render_to_response("about.html", dict(personal=personal, about=about, awards=awards, user=request.user,
                                                 media_url=MEDIA_URL, static_url=STATIC_URL))


def tickets(request):
    """tickets listing."""
    if request.is_ajax():
        if 'pk' in request.POST.keys() and '3' in request.POST.keys():
            _type = TypeWork.objects.get(type_work=request.POST['11'])
            status = TicketStatus.objects.get(name=request.POST['19'])
            Ticket.objects.filter(pk=request.POST['pk']).update(first_name=request.POST['3'],
                                                                last_name=request.POST['5'],
                                                                email=request.POST['7'],
                                                                phone=request.POST['9'],
                                                                type_work=_type,
                                                                date=request.POST['13'], time=request.POST['15'],
                                                                description=request.POST['17'],
                                                                status=status,
                                                                viewed=True)
    tickets = Ticket.objects.all()
    status = TicketStatus.objects.all()
    status_count = TicketStatus.objects.all().count() > 1
    count = Ticket.objects.filter(viewed=False).count()

    return render_to_response("tickets.html",
                              dict(tickets=tickets, user=request.user, status=status, count=count,
                                   media_url=MEDIA_URL, static_url=STATIC_URL),
                              context_instance=RequestContext(request))


def portfolio(request):
    """about listing."""
    images = Image.objects.all()

    return render_to_response("portfolio.html", dict(images=images, user=request.user,
                                                     media_url=MEDIA_URL, static_url=STATIC_URL))


def stats(requset):
    return render_to_response("stats.html")


def contacts(request):
    """about listing."""
    personal = Personal.objects.all()[0]

    return render_to_response("contacts.html", dict(personal=personal, user=request.user,
                                                    media_url=MEDIA_URL, static_url=STATIC_URL))


def signup(request):
    """about listing."""
    type_works = TypeWork.objects.all()
    signup = TextBlock.objects.filter(tag__name__contains='signup')
    return render_to_response("signup.html", dict(signup=signup, type_works=type_works, user=request.user,
                                                  media_url=MEDIA_URL, static_url=STATIC_URL),
                              context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    images = Image.objects.all()
    slides = Slide.objects.all()
    short_by_me = TextBlock.objects.filter(tag__name__contains='short_by_me')
    contacts = Personal.objects.all()[0]
    type_works = TypeWork.objects.all()
    return render_to_response("home.html", dict(images=images, type_works=type_works, contacts=contacts, slides=slides,
                                                short_by_me=short_by_me, user=request.user,
                                                media_url=MEDIA_URL, static_url=STATIC_URL),
                              context_instance=RequestContext(request)
                              )