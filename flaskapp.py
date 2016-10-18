@app.route('/')
def root():
    return 'hello flask.'

@app.route('/greet/<name>')
def greet(name):
    return 'Hello '+name
