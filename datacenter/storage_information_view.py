import datetime
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        who_entered = visit.passcard.owner_name
        entered_at = localtime(visit.entered_at)
        duration = visit.get_duration()
        non_closed_visits.append(
            {
                'who_entered': who_entered,
                'entered_at': entered_at,
                'duration': visit.format_duration(duration),
                'is_strange': visit.is_visit_long()
            }
        )
    context = {
        'non_closed_visits': non_closed_visits, 
    }
    return render(request, 'storage_information.html', context)

