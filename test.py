from flask import Flask

@app.route('/')
def hello_world():
    return 'Hello World'

app.run(port=5000)
