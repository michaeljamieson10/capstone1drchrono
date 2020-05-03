from flask import Flask, render_template, request, redirect, jsonify, make_response, session
import requests
import datetime
import json
# from flask_cors import CORS, cross_origin 
app = Flask(__name__)
# CORS(app)
app.config["SECRET_KEY"] = "SSHH SECRETO"



def header_create():
    access_token = session['access_token']
    headers={
    'Authorization':'Bearer %s' %access_token,
    'Content-type':"application/json"
    }
    return headers



@app.route("/", methods=["GET", "POST"])
def homepage():
    """Show homepage."""
    
    return render_template("index.html")
@app.route("/login", methods=["GET", "POST"])
def loginpage():
    """Show homepage."""
    
    return render_template("login.html")

@app.route("/authorized", methods=["POST"])
def authorization():
    """Show homepage."""
    redirect_uri = 'http://127.0.0.1:5000/token'
    client_id = 'IvnxhWMo16B9BQBVs89XfvEWYgDrPch5ZGnwCBvK'
    url = f"https://drchrono.com/o/authorize/?redirect_uri={redirect_uri}&response_type=code&client_id={client_id}"
    res = requests.get(url)
    return redirect(url)

@app.route("/token", methods=["GET", "POST"])
def token():
    """redirec to token page."""

    response = requests.post('https://drchrono.com/o/token/', data={
        'code': request.args.get('code'),
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://127.0.0.1:5000/token',
        'client_id': 'IvnxhWMo16B9BQBVs89XfvEWYgDrPch5ZGnwCBvK',
        'client_secret': 'BHHd5xFV1arUnXykMl5CRiSKu8q6GFNCEcgKVyYMZktalOo2VE3dZlG8z94QJoaUT9RuMCf8OWehrKz0Vj4ShrXLmA6GHCBwGUJdqP0dUiJbf9xKhAVwuDEltTz4n3qw',
    })
    response.raise_for_status()
    data = response.json()
    # Save these in your database associated with the user
    session['access_token'] =  data['access_token']
    session['refresh_token'] =  data['refresh_token']
    return redirect("/")

@app.route("/doctor")
def list_doctor():
    """Will list doctors"""
    url = "https://app.drchrono.com/api/doctors"
    response = requests.get(url, headers=header_create())
    response.raise_for_status()
    data = response.json()
    raise
    return redirect('/')


@app.route("/user")
def user():
    """Will list current user"""
    url = "https://drchrono.com/api/users/current"
    response = requests.get(url, headers=header_create())
    response.raise_for_status()
    data = response.json()
    return redirect('/')

@app.route("/patients")
def list_patients():
    """Will list patients"""
    url = "https://app.drchrono.com/api/patients"
    
    response = requests.get(url, headers=header_create())
    response.raise_for_status()
    data = response.json()
    return render_template("patients.html", data=data['results'])

@app.route("/medications")
def list_medications():
    """Will list medications with patients in side bar menu"""
    url = "https://app.drchrono.com/api/medications"
    body = {
        "doctor": 266342,
        "patient" : 87214300
    }
    response = requests.get(url, headers=header_create(),data=json.dumps(body))
    response.raise_for_status()
    data = response.json()
    url = "https://app.drchrono.com/api/patients"
    response = requests.get(url, headers=header_create())
    response.raise_for_status()
    patient_data = response.json()
    raise
    return render_template("medications.html",data=data['results'], patient_data=patient_data['results'], access_token=session['access_token'])

@app.route("/patients/<patient_id>")
def list_patient(patient_id):
    """Will list patients"""
    url = f"https://app.drchrono.com/api/patients/{patient_id}"
    
    response = requests.get(url, headers=header_create())
    response.raise_for_status()
    data = response.json()
    return render_template("users/detail.html", data=data['results'])
@app.route("/patient_create")
def create_pt():
    """Will create patients """
    url = "https://app.drchrono.com/api/patients"
    body = {
        'doctor': 266342,
        'first_name': 'John',
        'last_name': 'Jamieson',
        'date_of_birth': '1997-03-31',
        'gender': 'Male'
    }

    response = requests.post(url,headers=header_create(), data=json.dumps(body))
    response.raise_for_status()
    data = response.json()
    return response.json()

    