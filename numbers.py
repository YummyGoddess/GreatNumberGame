from flask import Flask, importjrandom, render_templates, sessions, request, redirect
app = Flask(__name__)

@app.rout('/')
def index():
    return render_templates('index.html')
