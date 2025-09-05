from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.template import loader
from django.http import HttpResponse, HttpRequest
from django.contrib import admin
from django.conf import settings
from studies.models import Study, Subject
from datetime import datetime
from django.utils import timezone

# Create your views here.
def index(request:HttpRequest):
    user_required = settings.OBSERVER_USER_REQUIRED
    if "username" in request.POST and \
        "software" in request.POST and \
        (not user_required or ("password" in request.POST and \
        _login(request.POST["username"], request.POST["password"]))):

        request.session["user"] = request.POST["username"]
        return redirect("study", study=request.POST["software"])
    else:
        template = loader.get_template('software.html')
        context = {
            "login_required": user_required
        }
        return HttpResponse(template.render(context, request))

def _login(user, password):
    try:
        u = User.objects.get(username=user)
        return check_password(password, u.password)
    except:
        return False

def study(request:HttpRequest, study):
    if "institution" in request.POST:
        return redirect("subjects", study=study, institution=request.POST["institution"], trial=request.POST["trial"])
    else:
        template = loader.get_template('study.html')
        context = {
            "study": study,
            "institution": request.GET["institution"] if "institution" in request.GET else ""
        }

        return HttpResponse(template.render(context, request))
    
def subjects(request:HttpRequest, study, institution, trial):
    try:
        s = Study.objects.get(software=study, institution=institution, trial=trial)
    except:
        s = None

    if "subjects" in request.POST:
        if s is None:
            s = Study(
                username=request.session['user'],
                software=study,
                institution=institution,
                trial=trial,
                behavior="PSLCBEHAVIORV1",
                affect="PSLCAFFECTV1",
                intervention="nop"
                )
            s.save()
        else:
            s.subject_set.all().delete()

        for i, stud in enumerate(request.POST.getlist("subject_id")):
            s.subject_set.create(
                number=i+1, 
                label=stud
                )
        return redirect("standby", study=study, institution=institution, trial=trial)
    else:
        template = loader.get_template('subjects.html')
        context = {
            "study": study,
            "institution": institution,
            "trial": trial
        }

        return HttpResponse(template.render(context, request))
    
def standby(request:HttpRequest, study, institution, trial):
        try:
            s = Study.objects.get(software=study, institution=institution, trial=trial)
        except:
            s = None
        
        if s is None:
            template = loader.get_template('standby_missing.html')
            context = {
                "study": study,
                "institution": institution,
                "trial": trial
            }

            return HttpResponse(template.render(context, request))
        elif s.localtime is not None:
            template = loader.get_template('standby_reject.html')
            context = {
                "study": study,
                "institution": institution,
                "trial": trial
            }

            return HttpResponse(template.render(context, request))
        if "localtime" in request.POST:
            s.localtime = datetime.fromtimestamp(float(request.POST["localtime"])/1000)
            s.servertime = timezone.now()
            s.save()
            return redirect("records", session=s.session)
        else:
            template = loader.get_template('standby.html')
            context = {
                "study": study,
                "institution": institution,
                "trial": trial
            }

            return HttpResponse(template.render(context, request))
        
# Admin site
@admin.site.admin_view
def studies(request:HttpRequest):
    s = Study.objects.all()
    template = loader.get_template('studies.html')
    context = {
        "studies": s,
    }

    return HttpResponse(template.render(context, request))