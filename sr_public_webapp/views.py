import datetime, json, logging

import trio
from django.conf import settings as settings_project
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from sr_public_webapp import settings_app
from sr_public_webapp.lib import version_helper
from sr_public_webapp.lib.version_helper import GatherCommitAndBranchData


log = logging.getLogger(__name__)


# -------------------------------------------------------------------
# main urls
# -------------------------------------------------------------------


def info(request):
    return HttpResponseRedirect( settings_app.INFO_URL_REDIRECT )


def sample_string_var(request):
    var = 'Just a string-variable here; nothing to see.'
    context = { 'var_key': var }
    if request.GET.get('format', '') == 'json':
        resp = HttpResponse( json.dumps(context, sort_keys=True, indent=2), content_type='application/json; charset=utf-8' )
    else:
        resp = render( request, 'sr_public_webapp_templates/template_testing.html', context )
    return resp


def sample_array(request):
    array = [ 'one', 'two', 'three' ]
    context = { 'array_key': array }
    if request.GET.get('format', '') == 'json':
        resp = HttpResponse( json.dumps(context, sort_keys=True, indent=2), content_type='application/json; charset=utf-8' )
    else:
        resp = render( request, 'sr_public_webapp_templates/template_testing.html', context )
    return resp


def sample_json_array(request):
    person_A = { 'first_name': 'emma', 'last_name': 'goldman' }
    person_B = { 'first_name': 'frida', 'last_name': 'kahlo' }
    person_C = { 'first_name': 'eleanor', 'last_name': 'roosevelt' }
    people = [ person_A, person_B, person_C ]
    context = { 'people_key': people }
    if request.GET.get('format', '') == 'json':
        resp = HttpResponse( json.dumps(context, sort_keys=True, indent=2), content_type='application/json; charset=utf-8' )
    else:
        resp = render( request, 'sr_public_webapp_templates/template_testing.html', context )
    return resp


def sample_browse_via_url_load(request):
    return HttpResponse( "response from `browse_via_url_load()` coming" )


def sample_browse_via_file_load(request):
    return HttpResponse( "response from `browse_via_file_load()` coming" )


# -------------------------------------------------------------------
# support urls
# -------------------------------------------------------------------


def error_check( request ):
    """ For an easy way to check that admins receive error-emails (in development)...
        To view error-emails in runserver-development:
        - run, in another terminal window: `python -m smtpd -n -c DebuggingServer localhost:1026`,
        - (or substitue your own settings for localhost:1026)
    """
    log.debug( f'project_settings.DEBUG, ``{settings_project.DEBUG}``' )
    if settings_project.DEBUG == True:
        log.debug( 'triggering exception' )
        raise Exception( 'Raising intentional exception.' )
    else:
        log.debug( 'returing 404' )
        return HttpResponseNotFound( '<div>404 / Not Found</div>' )


def version( request ):
    """ Returns basic branch and commit data. """
    rq_now = datetime.datetime.now()
    gatherer = GatherCommitAndBranchData()
    trio.run( gatherer.manage_git_calls )
    commit = gatherer.commit
    branch = gatherer.branch
    info_txt = commit.replace( 'commit', branch )
    context = version_helper.make_context( request, rq_now, info_txt )
    output = json.dumps( context, sort_keys=True, indent=2 )
    log.debug( f'output, ``{output}``' )
    return HttpResponse( output, content_type='application/json; charset=utf-8' )


def root( request ):
    return HttpResponseRedirect( reverse('info_url') )
