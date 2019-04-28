from flask import Flask
from flask import Response
from flask import request
from flask_cors import CORS
from lamdaCalls import getCredit, verifySite, verifyEmail, getFullContact
from mysql import connector
import json

app = Flask(__name__)
CORS(app)

def validate_body(expected, actual):
    for param in expected:
        if param not in actual:
            return False
    return True

def insertCredit(values):
    credib = connector.connect(
        host="credibit.crcsqwhwrqwu.us-east-2.rds.amazonaws.com",
        user="credi",
        passwd="bit12345",
        database="credidev"
    )

    cursor = credib.cursor(dictionary=True)

    sql = "INSERT INTO creditRequest (nombreEmpresa, correo, puntosBuro, puntosSat,\
            ingresoMensual, ingresoNeto, cantidadDeseada, plazoDeseado, companySite,\
            toPay, approved, twitter, linkedin, facebook, founded, employees) VALUES\
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    vals = (values['nombreEmpresa'], values['correo'],
            values['puntosBuro'], values['puntosSat'], values['ingresoMensual'],
            values['ingresoNeto'], values['cantidadDeseada'], values['plazoDeseado'],
            values['companySite'], values['toPay'], values['approved'], values['twitter'],
            values['linkedin'], values['facebook'], values['founded'], values['employees'])

    cursor.execute(sql, vals)

    credib.commit()

    cursor.close()

@app.route("/")
def hello():
    return "API is alive"

@app.route("/creditEligibility", methods=['POST'])
def getCreditEligibility():
    expected_values = ['nombreEmpresa', 'correo', 'puntosBuro', 'puntosSat', 'cantidadDeseada', 'plazoDeseado', 'ingresoMensual', 'ingresoNeto', 'companySite']
    body = request.json

    valid = validate_body(expected_values, body)

    credit_input = {
        'puntosBuro': body['puntosBuro'],
        'puntosSat': body['puntosSat'],
        'ingresoMensual': body['ingresoMensual'],
        'ingresoNeto': body['ingresoNeto'],
        'cantidadDeseada': body['cantidadDeseada'],
        'plazoDeseado': body['plazoDeseado']
    }

    validSite = verifySite(body['companySite'], body['nombreEmpresa'])
    validMail = verifyEmail(body['correo'])

    response = ''

    if not validSite or not validMail:
        response = {
            'is_valid': False
        }
    else:
        response = getCredit(credit_input)
    
    comp_data = getFullContact(body['companySite'])

    insert_credit = {
        'nombreEmpresa': body['nombreEmpresa'],
        'correo': body['correo'],
        'puntosBuro': body['puntosBuro'],
        'puntosSat': body['puntosSat'],
        'ingresoMensual': body['ingresoMensual'],
        'ingresoNeto': body['ingresoNeto'],
        'cantidadDeseada': body['cantidadDeseada'],
        'plazoDeseado': body['plazoDeseado'],
        'companySite': body['companySite'],
        'approved': response['is_valid'],
        'twitter': comp_data['twitter'],
        'facebook': comp_data['facebook'],
        'linkedin': comp_data['linkedin'],
        'founded': comp_data['founded'],
        'employees': comp_data['employees']
    }

    insert_credit['toPay'] = response['ammount'] if response['is_valid'] else None

    insertCredit(insert_credit)

    return Response(json.dumps(response), content_type='application/json; charset=utf-8')

@app.route("/creditRequests")
def creditRequests():
    credib = connector.connect(
        host="credibit.crcsqwhwrqwu.us-east-2.rds.amazonaws.com",
        user="credi",
        passwd="bit12345",
        database="credidev"
    )

    cursor = credib.cursor(dictionary=True)

    cursor.execute("SELECT * FROM creditRequest")

    creditRequests = cursor.fetchall()

    cursor.close()

    return Response(json.dumps({"creditRequests": creditRequests}), content_type='application/json; charset=utf-8')

@app.route("/login", methods=['POST'])
def login():
    body = request.json

    username = body['username']
    password = body['password']

    credib = connector.connect(
        host="credibit.crcsqwhwrqwu.us-east-2.rds.amazonaws.com",
        user="credi",
        passwd="bit12345",
        database="credidev"
    )

    cursor = credib.cursor(dictionary=True)

    sql = "SELECT * FROM admin WHERE username='%s' and password='%s'" % (username, password)
    cursor.execute(sql)

    user = cursor.fetchone()

    cursor.close()

    if user is None:
        return Response("Not able to log in", status=401)
    else:
        return "Successful"