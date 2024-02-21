from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import BadRequest
from django.contrib import admin
from datetime import datetime
from django.utils import timezone
import csv
from studies.models import Study
from OSTHAR.hart import *
from .models import Record

# Create your views here.
def records(request:HttpRequest, session):
    s = Study.objects.get(session=session)
    return redirect('observation', session=session, subject_id=1)

def observation(request:HttpRequest, session, subject_id):
    s = Study.objects.get(session=session)
    sub = s.subject_set.get(number=subject_id)
    next_id = (subject_id) % s.subject_set.count() + 1
    if "subject_id" in request.POST:
        sub.record_set.create(
            localtime = datetime.fromtimestamp(float(request.POST["localtime"])/1000),
            servertime = timezone.now(),
            behavior = request.POST["behavior"],
            affect = request.POST["affect"],
            intervention = request.POST["intervention"],
        )
        if "finish" in request.POST:
            s.localendtime = datetime.fromtimestamp(float(request.POST["localtime"])/1000)
            s.serverendtime = timezone.now()
            s.save()
            return redirect('results', session=session)
        else:
            return redirect('observation', session=session, subject_id=next_id)
    else:
        template = loader.get_template('observation.html')
        obs = Record.objects.raw("SELECT * FROM records_record WHERE subject_id in (SELECT id from studies_subject where study_id = %s) ORDER BY id desc;", [s.pk])
        context = {
            "session": session,
            "study": s.software,
            "institution": s.institution,
            "trial": s.trial,
            "subject_id": subject_id,
            "next_subject_id": next_id,
            "label": sub.label,
            "affects": get_affects(s.affect),
            "behaviors": get_behaviors(s.behavior),
            "latest_records": obs[:3],
            "observations": len(obs),
        }
        return HttpResponse(template.render(context, request))
    
def results(request:HttpRequest, session):
    template = loader.get_template('results.html')
    s = Study.objects.get(session=session)
    obs = Record.objects.raw("SELECT * FROM records_record WHERE subject_id in (SELECT id from studies_subject where study_id = %s) ORDER BY id desc;", [s.pk])
    context = {
            "session": session,
            "study": s.software,
            "start_time": s.servertime,
            "records": obs,
            "observations": len(obs),
        }
    return HttpResponse(template.render(context, request))

# Admin sites

@admin.site.admin_view
def export(request:HttpRequest, session):
    s = Study.objects.get(session=session)
    records = Record.objects.raw("SELECT * FROM records_record WHERE subject_id in (SELECT id from studies_subject where study_id = %s) AND Exclude = False ORDER BY id desc;", [s.pk])
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{s}.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(["FILE HEADER KEY:", "username", "software", "institution", "trial", "numsubjects", "behavior", "affect", "localtime", "servertime", "intervention"])
    writer.writerow([s.username, s.software, s.institution, s.trial, s.subject_set.count(), s.behavior, s.affect, s.localtime, s.servertime, s.institution])
    writer.writerow(["FILE DATA KEY:", "subject", "offsetfromstart", "behavior", "affect", "intervention"])
    for record in records:
        writer.writerow([record.subject.label, record.servertime-s.servertime, record.behavior, record.affect, record.intervention])
    return response

# Ajax apis

def record(request:HttpRequest, session, record_id):
    r = Record.objects.get(pk=record_id)
    if r.subject.study.session != session:
        return BadRequest()
    else:
        if "mark" in request.POST:
            r.marked = request.POST["mark"]
        if "note" in request.POST:
            r.note = request.POST["note"]
        if "exclude" in request.POST:
            r.exclude = request.POST["exclude"]
        r.save()
        return HttpResponse("OK")