from cProfile import run
from flask import Flask, render_template, redirect, request, session
# The Session instance is not used for direct access, you should always use flask.session
from flask_session import Session
from forms import Deltagare, Budget, Längd, Tema, Plats, Jury, JuryNamn, Språk

app = Flask(__name__)
app.secret_key = "1234"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template('index.html')
 
 

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        session['lista'] = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        return redirect("/guide")
    return render_template("login.html")


 


@app.route("/guide", methods=["POST", "GET"])
def guide():
    #form0 = Namn()
    form1 = Tema()
    form2 = Deltagare()
    form3 = Längd()
    form4 = Budget()
    form5 = Plats()
    form6 = Jury()
    form7 = JuryNamn()
    form8 = Språk()
    

    #if form0.validate():
    #    namn = request.form['namn']
    #    session['lista'][0]= namn 
    #    session.modified = True
       

    if form1.validate():
        tema = request.form['tema']
        session['lista'][1] = tema 
        session.modified = True
    
    if form2.validate():
        deltagare = request.form['deltagare']
        session['lista'][2] = deltagare 
        
        deltagare = int(deltagare) 

        if deltagare < 7:
            session['lista'][3] = "Vi rekommenderar att ni har flera deltagare för att kunna ha några grupper som kommer på lösningar. "
        elif 8 <= deltagare <= 8:
            session['lista'][3] = "Vi rekommenderar att dela in era deltagare i två olika grupper bestående av fyra personer i vardera. Grupper med fyra personer har visat sig fungera mest optimalt under ett hackaton."
        elif 9 <= deltagare <= 12:
            session['lista'][3] = "Vi rekommenderar att dela in era deltagare i tre olika grupper bestående av tre till fyra personer i vardera. Grupper med fyra personer har visat sig fungera mest optimalt under ett hackaton."
        elif 13 <= deltagare <= 16:
            session['lista'][3] = "Vi rekommenderar att dela in era deltagare i fyra olika grupper bestående av tre till fyra personer i vardera. Grupper med fyra personer har visat sig fungera mest optimalt under ett hackaton."
        elif 17 <= deltagare <= 20:
            session['lista'][3] = "Vi rekommenderar att dela in era deltagare i fem olika grupper bestående av tre till fyra personer i vardera. Grupper med fyra personer har visat sig fungera mest optimalt under ett hackaton."
        elif 21 <= deltagare <= 24:
            session['lista'][3] = "Vi rekommenderar att dela in era deltagare i sex olika grupper bestående av tre till fyra personer i vardera. Grupper med fyra personer har visat sig fungera mest optimalt under ett hackaton."
        elif 25 <= deltagare <= 28:
            session['lista'][3] = "Vi rekommenderar att dela in era deltagare i sju olika grupper bestående av tre till fyra personer i vardera. Grupper med fyra personer har visat sig fungera mest optimalt under ett hackaton."
        elif 29 <= deltagare <= 32:
            session['lista'][3] = "Vi rekommenderar att dela in era deltagare i åtta olika grupper bestående av tre till fyra personer i vardera. Grupper med fyra personer har visat sig fungera mest optimalt under ett hackaton."
        elif 33 <= deltagare <= 36:
            session['lista'][3] = "Vi rekommenderar att dela in era deltagare i nio olika grupper bestående av tre till fyra personer i vardera. Grupper med fyra personer har visat sig fungera mest optimalt under ett hackaton."
        elif 34 <= deltagare <= 40:
            session['lista'][3] = "Vi rekommenderar att dela in era deltagare i tio olika grupper bestående av tre till fyra personer i vardera. Grupper med fyra personer har visat sig fungera mest optimalt under ett hackaton."
        else:
            session['lista'][3] = "Vi rekommenderar att dela in era deltagare i grupper bestående av fyra personer i vardera eftersom denna gruppstorlek har visat sig fungera mest optimalt under hackaton. "
        
        session.modified = True


    if form3.validate():
        längd = request.form['längd']
        session['lista'][4] = längd + ' h' 
        
        längd = int(längd) 

        if längd <= 6:
            session['lista'][5] = "Vi rekommenderar att ni använder minst en dag."
        elif 7 <= längd <= 12:
             session['lista'][5]= "Vi rekommenderar att ni använder två dagar."
        elif 13 <= längd <= 18: 
             session['lista'][5] = "Vi rekommenderar att ni använder tre dagar."
        elif 19 <= längd <= 24:
             session['lista'][5] = "Vi rekommenderar att ni använder fyra dagar"
        elif 25 <= längd <= 30:
             session['lista'][5] = "Vi rekommenderar att ni använder fem dagar"
        elif 31 <= längd <= 36:
             session['lista'][5] = "Vi rekommenderar att ni använder sex dagar"
        elif 37 <= längd <= 42:
            session['lista'][5] = "Vi rekommenderar att ni använder sju dagar"
        elif 43 <= längd <= 48:
            session['lista'][5] = "Vi rekommenderar att ni använder åtta dagar"
        else:
            session['lista'][5] = "Mera än 48 h blir för långt."
        
        session.modified = True


    if form4.validate():
        budget = request.form['budget']
        session['lista'][6] = budget + " €"

        budget = int(budget) 

        if budget < 500:
           session['lista'][7] = "Planera ert hackaton så att det finns budgetmedel som täcker kostnader för material och mellanmål. Exempel på material är post-it lappar, pennor och övriga kontorsmaterial. Mellanmål rekommenderas för att upprätthålla en god energinivå bland deltagarna under dagen/dagarna."
        else:
           session['lista'][7] = "Planera ert hackaton så att det finns budgetmedel som täcker kostnader för att ta in externa experter, material och mellanmål. Exempel på material är post-it lappar, pennor och övriga kontorsmaterial. Mellanmål rekommenderas för att upprätthålla en god energinivå bland deltagarna under dagen/dagarna. Experter kan tas in som inspiratörer och, eller jurymedlemmar."
         
        session.modified = True
    
    if form5.validate():
        plats = request.form['plats']
        session['lista'][8] = plats 
        session.modified = True
    

    
    if form6.validate():
        jury = request.form['jury']
        session['lista'][9] = jury
        jury = int(jury)

        if jury < 2: 
            session['lista'][10]= "Vi rekommenderar att ni gärna har fler än två jurym medlemmar."
        else: 
            session['lista'][10] = "Bra!" 

        session.modified = True
    

    if form7.validate():
        juryNamn = request.form['juryNamn']
        session['lista'][11] = juryNamn 
        session.modified = True
    
    if form8.validate():
        språk = request.form['språk']
        session['lista'][12] =  språk 
        session.modified = True
    
       
    return render_template("verktyg.html", form1 = form1, form2 = form2, form3 = form3, form4 = form4, form5 = form5, form6 = form6, form7 = form7, form8 = form8, Listan = session['lista'])





@app.route("/logout")

def logout():
    session["name"] = None
    return redirect("/")
 
 

if __name__ == "__main__":

    app.run(debug=True)
