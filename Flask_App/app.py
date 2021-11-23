from flask import Flask,request

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
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

        return url

    if(request.method=='GET'):
        return "Here by a GET request"



if __name__ == '__main__':
    app.run()
