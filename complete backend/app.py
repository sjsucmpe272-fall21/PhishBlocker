import flask
from flask import Flask, request,make_response
import ML.preprocessing
import mongo_db.phish_blocker_mongo_db as mongo_db

from flask_cors import CORS, cross_origin

#import ssl
#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#context.use_privatekey_file('key.pem')
#context.use_certificate_file('cert.pem')

#import ssl
#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#context.load_cert_chain('cert.pem', 'key.pem')

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
            url_list=[]
            pred_list=[]
            ans_list=[]
            res=ML.preprocessing.url_pass(s[i])
            for j in range(len(res)):
                D1={}
                if(res[j][0]==1):
                    #url_list.append(s[i][j])
                    #pred_list.append(res[j][1])
                    D1['url']=s[i][j]
                    D1['prediction']=res[j][1]
                    ans_list.append(D1)



                #temp.append(j)
            #url[i]=url_list
            #url['prediction']=pred_list
            url[i]=ans_list
        #resp=flask.make_response(url)
        #header = resp.headers
        #resp.headers['Access-Control-Allow-Origin'] = '*'
        return url

    if(request.method=='GET'):
        #resp = flask.Response("Here by a GET request")
        #header = resp.headers
        #resp.headers['Access-Control-Allow-Origin'] = '*'
        #resp.headers['X-Content-Type-Options'] = 'nosniff'
        #c=test()
        #url_example = ["http://9779.info/%E4%BA%94%E8%B0%B7%E6%9D%82%E7%B2%AE%E4%BA%BA%E7%89%A9%E7%B2%98%E8%B4%B4%E7%94%BB/"]
        #c = ML.preprocessing.extract_features(["www.google.com"])
        c=ML.preprocessing.url_pass(["www.google.com"])
        #print(c)
        return "GREAT WORKING"


@app.route('/db', methods=['POST'])
@cross_origin()
def db_hello():  # put application's code here
    if (request.method == 'POST'):
        s = request.get_json()
        mongo_inst = mongo_db.PhishBlockerMongoDB()

        for i in s:
            mongo_inst.insert_url(s[i], "safe")

        return "success"


if __name__ == '__main__':
    #app.run(ssl_context='adhoc')
    #app.run(ssl_context=("cert.pem", "key.pem"))
    #app.run(host='0.0.0.0',port=8080)
    app.run()

