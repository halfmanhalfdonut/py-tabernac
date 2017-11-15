from flask import Flask, request, jsonify
from src.controllers.home import Home
from src.controllers.praise_him import PraiseHim

app = Flask(__name__)

@app.route("/")
def home():
  return Home().randomize()

@app.route("/praise-him", methods = ["POST"])
def praise_him():
  return PraiseHim().handle(dict(request.form))

@app.errorhandler(404)
def not_found(error):
  return jsonify({ "status": 404, "message": "Not found" })

@app.errorhandler(500)
def error(error):
  return jsonify({ "status": 500, "message": "Error" })