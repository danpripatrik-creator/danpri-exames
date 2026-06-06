
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pdfplumber
import re
import io
import os

app = Flask(__name__)
CORS(app, origins="*")

def extrair_alunos(texto):
    alunos = []
    linhas = texto.split("\n")
    for linha in linhas:
        l = linha.strip()
        m = re.match(r"^(\d{1,3})-\s+([A-Z][A-Z\s]{2,20}?)\s+(?:[A-Z]+\s+)+\(\d\)([AB\/]+)\s+([A-Z0-9]{3}-?[0-9A-Z]{3,4})\s+OK.*(\d{2}:\d{2})", l)
        if m:
            alunos.append({"nome": m.group(2).strip(), "cpf": "", "cat": m.group(3), "placa": m.group(4), "hr": m.group(5)})
            continue
        m3 = re.match(r"^(\d{1,2})\s+([A-Z][A-Z\s]{3,60})\s+(\d{3}\.\d{3}\.\d{3}-\d{2})\s+([AB\/]+)", l)
        if m3:
            alunos.append({"nome": m3.group(2).strip(), "cpf": m3.group(3), "cat": m3.group(4), "placa": "", "hr": "08:00"})
            continue
        m1 = re.match(r"(\d{3}\.\d{3}\.\d{3}-\d{2})\s+SP-", l)
        if m1:
            cpf = m1.group(1)
            catM = re.search(r"----\s*(AB|A\/B|A|B)", l) or re.search(r"\b(AB|A\/B|A|B)\s*$", l)
            cat =
