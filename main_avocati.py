from flask import flask, render_template, request, redirect, url_for
#import Avocati as a

app = flask(__name__)

@app.route("/autentificare", methods=['POST',"GET"])  
def GenerateReport():
    if request.method == 'POST':
        data = request.form['filename']
        #filename = a.process_data(data)
        
        return render_template("Autentificare.html",filename=data)

    return render_template("Autentificare.html")

@app.route("/display/<filename>")
def DisplayReport(filename):
    return redirect(url_for('Source',filename= '/files/'+filename),code=301)

@app.route("/meniu",methods=['GET'])
def GetMeniu():
    if request.method == 'GET':
        return render_template("Meniu.html")

@app.route("/despre",methods=['GET'])
def GetDespre():
    if request.method == 'GET':
        return render_template("Despre.html")
    
@app.route("/avocati",methods=['GET'])
def GetAvocati():
    if request.method == 'GET':
        return render_template("Avocati.html")

@app.route("/clienti",methods=['GET'])
def GetClienti():
    if request.method == 'GET':
        return render_template("Clienti.html")  


    
app.run(port=5000)