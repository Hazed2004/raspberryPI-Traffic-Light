from flask import Flask, render_template, request, Response
import flask.cli
import socket
from functools import wraps
import json
from hashlib import md5
from . import Firmware

htmlFolder = "./HTML"
PIWeb = Flask(__name__, template_folder= htmlFolder)
flask.cli.show_server_banner = lambda *args: None

authOpen = open("./library/auth.json", "rt")
authRead = authOpen.read()
authOpen.close()

def check_auth(username, password):
    authConfig = json.loads(authRead)
    return username == authConfig["UserName"] and password == authConfig["Password"]

def authenticate():
    return Response(
    'Could not verify your access level.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@PIWeb.route("/")
@requires_auth
def home():
    return render_template("index.html")

@PIWeb.route("/redon/", methods=['POST'])
def redledon():
    Firmware.OnRedSignal = True
    Firmware.OnGreenSignal = False
    Firmware.OnYellowSignal = False
    Firmware.OnAllSignal = False
    Firmware.OffRedSignal = False
    Firmware.OffGreenSignal = False
    Firmware.OffYellowSignal = False
    Firmware.OffAllSignal = False
    Firmware.AutomateTrafficSignal = False
    Firmware.LedController.OnRed()
    print("[+] Red light is turned on")
    return render_template('index.html');

@PIWeb.route("/redoff/", methods=['POST'])
def redledoff():
    Firmware.OnRedSignal = False
    Firmware.OnGreenSignal = False
    Firmware.OnYellowSignal = False
    Firmware.OnAllSignal = False
    Firmware.OffRedSignal = True
    Firmware.OffGreenSignal = False
    Firmware.OffYellowSignal = False
    Firmware.OffAllSignal = False
    Firmware.AutomateTrafficSignal = False
    Firmware.LedController.OffRed()
    print("[-] Red light is turned off")
    return render_template('index.html');

@PIWeb.route("/greenon/", methods=['POST'])
def greenledon():
    Firmware.OnRedSignal = False
    Firmware.OnGreenSignal = True
    Firmware.OnYellowSignal = False
    Firmware.OnAllSignal = False
    Firmware.OffRedSignal = False
    Firmware.OffGreenSignal = False
    Firmware.OffYellowSignal = False
    Firmware.OffAllSignal = False
    Firmware.AutomateTrafficSignal = False
    Firmware.LedController.OnGreen()
    print("[+] Green light is turned on")
    return render_template('index.html');

@PIWeb.route("/greenoff/", methods=['POST'])
def greenledoff():
    Firmware.OnRedSignal = False
    Firmware.OnGreenSignal = False
    Firmware.OnYellowSignal = False
    Firmware.OnAllSignal = False
    Firmware.OffRedSignal = False
    Firmware.OffGreenSignal = True
    Firmware.OffYellowSignal = False
    Firmware.OffAllSignal = False
    Firmware.AutomateTrafficSignal = False
    Firmware.LedController.OffGreen()
    print("[-] Green light is turned off")
    return render_template('index.html');

@PIWeb.route("/yellowon/", methods=['POST'])
def yellowledon():
    Firmware.OnRedSignal = False
    Firmware.OnGreenSignal = False
    Firmware.OnYellowSignal = True
    Firmware.OnAllSignal = False
    Firmware.OffRedSignal = False
    Firmware.OffGreenSignal = False
    Firmware.OffYellowSignal = False
    Firmware.OffAllSignal = False
    Firmware.AutomateTrafficSignal = False
    Firmware.LedController.OnYellow()
    print("[+] Yellow light is turned on")
    return render_template('index.html');

@PIWeb.route("/yellowoff/", methods=['POST'])
def yellowledoff():
    Firmware.OnRedSignal = False
    Firmware.OnGreenSignal = False
    Firmware.OnYellowSignal = False
    Firmware.OnAllSignal = False
    Firmware.OffRedSignal = False
    Firmware.OffGreenSignal = False
    Firmware.OffYellowSignal = True
    Firmware.OffAllSignal = False
    Firmware.AutomateTrafficSignal = False
    Firmware.LedController.OffYellow()
    print("[-] Yellow light is turned off")
    return render_template('index.html');    

@PIWeb.route("/allon/", methods=['POST'])
def allledon():
    Firmware.OnRedSignal = False
    Firmware.OnGreenSignal = False
    Firmware.OnYellowSignal = False
    Firmware.OnAllSignal = True
    Firmware.OffRedSignal = False
    Firmware.OffGreenSignal = False
    Firmware.OffYellowSignal = False
    Firmware.OffAllSignal = False
    Firmware.AutomateTrafficSignal = False
    Firmware.LedController.Onall()
    print("[+] All lights are turned on")
    return render_template('index.html');

@PIWeb.route("/trafficlight/", methods=['POST'])
def allledoff():
    Firmware.OnRedSignal = False
    Firmware.OnGreenSignal = False
    Firmware.OnYellowSignal = False
    Firmware.OnAllSignal = False
    Firmware.OffRedSignal = False
    Firmware.OffGreenSignal = False
    Firmware.OffYellowSignal = False
    Firmware.OffAllSignal = False
    Firmware.AutomateTrafficSignal = True
    Firmware.LedController.AutomateTraffic()
    print("[+] Traffic automation turned on")
    return render_template('index.html');

@PIWeb.route("/alloff/", methods=['POST'])
def automateTrafficLed():
    Firmware.OnRedSignal = False
    Firmware.OnGreenSignal = False
    Firmware.OnYellowSignal = False
    Firmware.OnAllSignal = False
    Firmware.OffRedSignal = False
    Firmware.OffGreenSignal = False
    Firmware.OffYellowSignal = False
    Firmware.OffAllSignal = True
    Firmware.AutomateTrafficSignal = False
    Firmware.LedController.Offall()
    print("[-] All lights are turned off")
    return render_template('index.html');

def Start():
    PIWeb.run(host= socket.gethostbyname(socket.gethostname()), port=12345)