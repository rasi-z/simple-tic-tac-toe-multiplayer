from flask import Flask,request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/data",methods=['GET'])
def s():
     with open('ids.txt', 'r') as jj:
          iid=jj.read()
     with open('states.txt', 'r') as uu:
          sst=uu.read()
     return  '{} {}'.format(iid,sst)

@app.route("/",methods=['GET'])
def sec():
    token=request.args.get('token')
    id=request.args.get('ids')
    uustate=request.args.get('static')
    with open('ids.txt', 'w') as f:
         f.write(id)
    with open('states.txt', 'w') as kk:
          kk.write(uustate)

    
    return  '{}{}'.format(id,uustate)

@app.route("/reset",methods=["GET"])
def reset():
     with open('ids.txt','w') as pm:
          pm.write(6)
     with open('states.txt','w') as km:
          km.write(6)