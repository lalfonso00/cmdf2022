from flask import Flask, render_template, request, redirect, url_for, escape

app = Flask(__name__)

@app.route('/', defaults={'mesg' : ''})       # when called without passing any values, the default would be an empty string
@app.route('/<string:mesg>', methods=['PUT'])                # default method is GET
def init(mesg):                             # this is a comment. You can create your own function name
    return '<h1>Welcome to Flask! </h1> {} '.format(mesg)

@app.route('/about', methods=['GET','POST','PUT'])
def your_url():
    if request.method == 'POST':
        print (request.form.get('dname'))
        return render_template('about.html', name=request.form.get('dname', 'No data passed')) # http://54.243.250.140:5000/about , body and form-data w/ Postman
        # request.form.get if method=POST
        # request.args.get if method=GET
    elif request.method == 'GET' :
        return redirect('/')   # calling init through the route '/' 
    else:
        return redirect(url_for('init',mesg='Under construction'), code=307)  # calling init function, code = 307 preserve http request


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)   # host='0.0.0.0' means whatever your public ip assigned will be used

# to test: use RestMan extensions in chrome