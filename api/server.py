from flask import Flask
from flask import Response
from flask_cors import CORS
from mysql import connector
import json
app = Flask(__name__)

CORS(app)

@app.route("/")
def hello():
    return "API is alive"

@app.route("/companies")
def companies():
    credib = connector.connect(
        host="credibit.crcsqwhwrqwu.us-east-2.rds.amazonaws.com",
        user="credi",
        passwd="bit12345",
        database="credidev"
    )

    cursor = credib.cursor(dictionary=True)

    cursor.execute("SELECT * FROM company")

    companies_result = []
    companies_fields = ["name", "twitter", "linkedin", "facebook", "website", "founded", "employees"]

    companies = cursor.fetchall()

    for company in companies:
        tmp_company = {}
        for field in companies_fields:
            tmp_company[field] = company[field]
        companies_result.append(tmp_company)

    return Response(json.dumps({"companies": companies_result}), content_type='application/json; charset=utf-8')