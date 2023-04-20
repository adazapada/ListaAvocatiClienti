from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route("/autentificare", methods = ['POST','GET'])
def DisplayHomePage():
    if request.method == 'POST':
        print("DisplayHomePage")
        print(request.form)
        email = request.form['email']
        password = request.form['password']
        if login(email, password) == True:
            return redirect("trimite")
        else:
            print("Login failed")
        
        
    return render_template("Autentificare.html")

@app.route("/trimite", methods = ['POST','GET'])
def trimite():
    print("DisplayMeniuPage")
    return render_template("Trimite.html")

@app.route("/despre",methods=['GET'])
def GetDespre():
    if request.method == 'GET':
        return render_template("Despre.html")
    
@app.route("/avocati",methods=['GET'])
def GetAvocati():
    if request.method == 'GET':
        return render_template("Echipa.html")

@app.route("/clienti",methods=['GET'])
def GetClienti():
    if request.method == 'GET':
        return render_template("Clienti.html")  


    
app.run(port=5000)