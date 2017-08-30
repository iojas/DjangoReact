# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *

# Create your views here.
def home(req):
  return render(req,'home.html')

def all_bands(req):
  return render(req,'band/all_bands.html')


def band(req, band_id):
  band = Band.objects.get(pk = band_id)
  return render(req,'band/band.html', {'band':band})
