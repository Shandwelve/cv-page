from app import app
from app.data import cv_data
from flask import jsonify, Response


@app.route("/personal", methods=["GET"])
def get_personal_info() -> Response:
    return jsonify({"results": cv_data["personal"]})


@app.route("/experience", methods=["GET"])
def get_experience() -> Response:
    return jsonify({"results": cv_data["experience"]})


@app.route("/education", methods=["GET"])
def get_education() -> Response:
    return jsonify({"results": cv_data["education"]})


@app.route("/languages", methods=["GET"])
def get_languages() -> Response:
    return jsonify({"results": cv_data["languages"]})
