from flask import Flask, render_template, request, redirect, jsonify, make_response, session
import requests
import random

app = Flask(__name__)

app.config["SECRET_KEY"] = "SSHH SECRETO"

@app.route("/", methods=["GET", "POST"])
def homepage():
    """Show homepage."""
    
    return render_template("index.html")

@app.route("/authorized", methods=["POST"])
def authorization():
    """Show homepage."""
    redirect_uri = 'http://127.0.0.1:5000/token'
    client_id = 'IvnxhWMo16B9BQBVs89XfvEWYgDrPch5ZGnwCBvK'
    # secret = ''
    url = f"https://drchrono.com/o/authorize/?redirect_uri={redirect_uri}&response_type=code&client_id={client_id}"
    res = requests.get(url)
    return redirect(f"{url}")

@app.route("/token", methods=["GET", "POST"])
def token():
    """redirec to token page."""
    # if 'error' in get_params:
        # raise ValueError('Error authorizing application: %s' % get_params[error])

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

    response_two = requests.post('https://drchrono.com/o/token/', data={
    'refresh_token': session['refresh_token'],
    'grant_type': session['refresh_token'],
    'client_id': 'IvnxhWMo16B9BQBVs89XfvEWYgDrPch5ZGnwCBvK',
    'client_secret': 'BHHd5xFV1arUnXykMl5CRiSKu8q6GFNCEcgKVyYMZktalOo2VE3dZlG8z94QJoaUT9RuMCf8OWehrKz0Vj4ShrXLmA6GHCBwGUJdqP0dUiJbf9xKhAVwuDEltTz4n3qw',
})
    return redirect("/")

@app.route("/doctor")
def list_doctor():
    """Will list doctors"""

    # This returns a 401

    # import pdb; pdb.set_trace()
    response = requests.get('https://app.drchrono.com/api/doctors', data={
        'access_token': session['access_token'],
    })
    response.raise_for_status()
    print(session['access_token'])
    raise
    return jsonify(response)

@app.route("/patients")
def list_patients():
    """Will list patients"""

    # This returns a 401

    # import pdb; pdb.set_trace()
    response = requests.get('https://app.drchrono.com/api/patients', data={
        'access_token': session['access_token'],
    })
    response.raise_for_status()
    print(session['access_token'])
    raise
    return jsonify(response)

@app.route("/patient_create")
def create_pt():
    """Will create patients """

    # This returns a 401

    response = requests.post('https://app.drchrono.com/api/patients', data={
        'token': session['access_token'],
        'chart_id': '1',
        'date_of_birth': '03/31/1995',
        'doctor': 1,
        'email': 'j@gmail.com',
        'ethnicity': 'Asian',
        'first_name': 'Michael',
        'gender': 'Male',
        'last_name': 'Jamieson',
        'preferred_langage': 'English',
        'race': 'Italian',
        'since': '4/28/20',
    })
    response.content
    raise
    return response.json()

    