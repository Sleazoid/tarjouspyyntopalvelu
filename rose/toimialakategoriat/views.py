# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from toimialakategoriat.models import Contact, Toimiala


def contacts(request):
    latest_contact_list = Contact.objects.all().order_by('sukunimi')
    
    return render_to_response('phonebook/contacts.html',
		{'latest_contact_list': latest_contact_list,})

def contact_add(request):
    # sticks in a POST or renders empty form
    form = ContactForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        #This is where you might chooose to do stuff.
        #cmodel.name = 'test1'
        cmodel.save()
        return redirect(contacts)

    return render_to_response('phonebook/contact_add.html',
                              {'contact_form': form},
                              context_instance=RequestContext(request))
                              
def contact_edit(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        contact = form.save()
        #this is where you might choose to do stuff.
        #contact.name = 'test'
        contact.save()
        return redirect(contacts)

    return render_to_response('phonebook/contact_edit.html',
                              {'contact_form': form,
                               'contact_id': contact_id},
                              context_instance=RequestContext(request))
                              
def contact_delete(request, contact_id):
    c = Contact.objects.get(pk=contact_id).delete()

    return redirect(contacts)                          
