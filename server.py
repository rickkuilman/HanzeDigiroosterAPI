import random
import string
import requests
import json

try:
  import env
except ImportError:
  print('env.py file not set')

import cherrypy

class DigiroosterAPI(object):
  _cp_config = {'tools.authorize.on': True}

  def __init__(self):
    self.session = requests.session()
    self.authenticate()

  def authenticate(self):
    self.session.get("https://intranet.hanze.nl/")

    response = self.session.post("https://intranet.hanze.nl/CookieAuth.dll?Logon", data = {
      "curl": "Z2F", # Yeah, I have no clue what this is either.
      "username": env.username,
      "password": env.password,
    })

    if response.status_code == 500:
      raise Exception("Login credentials incorrect")

  @cherrypy.tools.json_out()
  @cherrypy.expose
  def schools(self):
    response = self.session.post("https://digirooster.hanze.nl/website/AjaxService.asmx/GetSchools",
      headers = {
        'Content-type':'application/json'
    })

    return self.validateResponse(response)

  @cherrypy.expose
  @cherrypy.tools.json_out()
  def groups(self, schoolId, studyYear):
    response = self.session.post("https://digirooster.hanze.nl/website/AjaxService.asmx/GetGroups",
      headers = {
        'Content-type':'application/json'
      }, 
      data = json.dumps({
        'SchoolID': schoolId, 'StudyYear': studyYear
      })
    )

    return self.validateResponse(response)

  @cherrypy.tools.json_out()
  @cherrypy.expose
  def schedule(self, resourceID):
    response = self.session.post("https://digirooster.hanze.nl/website/AjaxService.asmx/GetSchedule",
      headers = {
        'Content-type':'application/json'
      }, 
      data = json.dumps({
        'ResourceID': resourceID, 'Resource':'2'
      })
    )

    return self.validateResponse(response)

  def validateResponse(self, response):
    return json.loads(json.loads(response.text)['d'])

def jsonify_error(status, message, traceback, version):
    response = cherrypy.response
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'status': status, 'message': message})

def authorize():
  if env.keepalive == True:
    digirooster.__init__()

if __name__ == '__main__':
  digirooster = DigiroosterAPI()

  cherrypy.config.update({'request.show_tracebacks': False})
  cherrypy.tools.authorize = cherrypy._cptools.HandlerTool(authorize)
  cp_config = { '/': {'error_page.404': jsonify_error}}

  cherrypy.quickstart(digirooster, config=cp_config)