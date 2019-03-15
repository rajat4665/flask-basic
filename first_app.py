# here I import flask library
from flask import Flask
app=Flask(__name__)

#this is stattic route ,here i set index function on my landing page
@app.route('/')
def index():
    return "<h1>Hello ,this is a landing page</h1>"
    #return method display this string in our landing page

#this is also static route, now i set "http://127.0.0.1:5000/about" to page function.
@app.route('/about')
def page():
    return "<h1>This is about page</h1>"
    # again return method display this string in our abour page

# here i used dynamic route (this type of route uses in page per user websites)
#<name> is dynamically change as per user input
#ttp://127.0.0.1:5000/user/rajat
@app.route('/user/<name>')
def users(name):
    return "<h1>User name is : {}</h1>".format(name)
    #here return display dynamic result with the help of string formating
if __name__=="__main__":
    app.run(debug=True)
    #app.run execute program and I enabled debug because this mode helps up catch errors.
