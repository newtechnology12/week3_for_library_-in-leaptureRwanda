import subprocess
import flask
from flask import Flask, request
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
import flask_restful

app = flask.Flask(__name__)

@app.route("/hello")
def hello_world():
  return "Hello, World!"


    
from flask_restplus import Api, Namespace, Resource, fields
api = Api()
api.init_app(app,title='Cisel Rest API', 
          description='Rest API for the CISEL project')
ns_default = api.default_namespace
ns_cisel = api.namespace('cisel-namespace', description='operations in the Cisel Namespace')
kubesecFields = ns_cisel.model('kubesec model', {
    'url': fields.String(description='URL Git repo', required=True),
    'folder': fields.String(description='Folder in the repo', required=True)
})

@ns_cisel.route('/mussa')
class KubeSec(Resource):
    @ns_cisel.doc(body=kubesecFields)
    def post(self):
        content = request.json
        urlGit = content['url']
        folder = content['folder']
        output = subprocess.check_output('git clone '+urlGit+'; cd '+folder+'; find . -type f -name "*.yaml" -exec kubesec scan {} \;', shell=True)
        return output.decode("utf-8")

if __name__ == "__main__":
    app.run(debug=True)
