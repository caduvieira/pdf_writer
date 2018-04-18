# -*- coding: utf-8 -*-
import hashlib
import hmac
import json
import os
from pyjasper.jasperpy import JasperPy
from flask import Flask, request, make_response


app = Flask(__name__)
input_file =  os.path.dirname(os.path.abspath(__file__)) + \
                 'templates/documento.jrxml'
jasper = JasperPy()
secret = b'123abc'


def compiling():
    jasper.compile(input_file)

def processing(parameters):
    output_file = os.path.dirname(os.path.abspath(__file__)) + 'output'
    jasper.process(
        input_file, output_file, parameters=parameters, format_list=["pdf"])

def filter_parameters(request_args):
    list_parameters = jasper.list_parameters(input_file)
    parameters = {}
    for key in list_parameters:
      if key in request_args:
        parameters[key] = request_args[key]
    return parameters

@app.route('/')
def my_route():

  parameters = filter_parameters(request.args.to_dict())

  sign = hmac.new(secret, json.dumps(parameters), hashlib.sha512).hexdigest()
  parameters['hash_value'] = sign
  processing(parameters)

  try:
      with app.open_resource(os.path.dirname(os.path.abspath(__file__)) + 'output/documento.pdf') as f:
          conteudo = f.read()
      resposta = make_response(conteudo)
      resposta.headers['Content-Type'] = 'application/pdf; charset=utf-8'
      resposta.headers['Content-Disposition'] = 'inline; filename=certificado_' + sign[:12] + '.pdf'
      return resposta
  except IOError:
      return make_response("<h1>403 Forbidden</h1>", 403)

@app.route("/validar/<hash_value>")
def check_hash(hash_value):
    if hash_value == "41b6b90efc34268fbaae7e142b9ee5412c996d901ec117f090bc3950138ffff77d0bc42e4d615d122a2f04a7a4ac68d9e2e7af7553aaae7dd43d088fa6d08cd0":
      return make_response("<h1>Hash correto</h1>", 200)
    else:
      return make_response("<h1>403 Inválido</h1>", 403)

if __name__ == '__main__':
    compiling()
    app.run(host='0.0.0.0')
