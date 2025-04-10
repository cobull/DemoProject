from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Inspection
from .models import Condition

@login_required
def display(request):
    inspections = Inspection.objects.all()
    return render(request, 'demo_home/display.html', {'inspections': inspections})

@login_required
def conditions(request, id):
    inspection = get_object_or_404(Inspection, id=id)
    conditions = Condition.objects.filter(Inspection=inspection)
    return render(request, 'demo_home/conditions.html', {'inspection': inspection, 'conditions': conditions})