from fastapi import FastAPI
from pydantic import BaseModel
from nameko.rpc import rpc
from nameko.standalone.rpc import ClusterRpcProxy


class User(BaseModel):
    username: str
    password: str
    email: str

class Login(BaseModel):
    username: str
    password: str

app = FastAPI()
broker_cfg = {'AMQP_URI': "amqp://guest:guest@rabbitmq"}


@app.post("/adduser/")
def api(user_item: User):
    with ClusterRpcProxy(broker_cfg) as rpc:
        sid = rpc.user.insert(
            user_item.username, user_item.password, user_item.email)
    return {'results': 'registered'}

@app.post("/login/")
def api(login_item: Login):
    with ClusterRpcProxy(broker_cfg) as rpc:
        rpc.userlogin.query(
            login_item.username, login_item.password)
    return {'results': 'login success'}
