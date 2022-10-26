#!/usr/bin/env python3
import os
from sys import argv
from pathlib import Path
from flask import Flask,request,redirect

outdir = Path(argv[1])
assert outdir.exists()
app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/static/index.html")
exiting = False
@app.route("/upload", methods=['POST'])
def upload_audio():
    global exiting
    f = request.files['myfile']
    fname = f.filename
    assert isinstance(fname, str)
    final_path = outdir.joinpath(fname)
    print(final_path,flush=True)
    final_path.write_bytes(f.read())
    exiting = True
    return 'Bye'

@app.teardown_request
def teardown(_):
    if exiting:
        os._exit(0)

if __name__ == '__main__':
    app.run("0.0.0.0")
