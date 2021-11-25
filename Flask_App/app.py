import flask
from flask import Flask, request,make_response

from flask_cors import CORS, cross_origin

#import ssl
#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#context.use_privatekey_file('key.pem')
#context.use_certificate_file('cert.pem')

import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert.pem', 'key.pem')

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['POST','GET'])
@cross_origin()
def hello_world():  # put application's code here
    if(request.method=='POST'):
        s = request.get_json()

        url={}
        #url.append(s[1])

        for i in (s):
            temp=[]
            for j in s[i]:
                temp.append(j)
            url[i]=temp
        resp=flask.make_response(url)
        header = resp.headers
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    if(request.method=='GET'):
        #resp = flask.Response("Here by a GET request")
        #header = resp.headers
        #resp.headers['Access-Control-Allow-Origin'] = '*'
        #resp.headers['X-Content-Type-Options'] = 'nosniff'
        return "HERE!!!"






if __name__ == '__main__':
    #app.run(ssl_context=context)
    app.run(ssl_context=("cert.pem", "key.pem"))
