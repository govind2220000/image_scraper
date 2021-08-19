from datetime import time
from flask import Flask, request, render_template, redirect
import time, datetime
import threading
 
from project_handler import run_scrapper
from logger.auto_logger import autolog

#s.enter()

def make_epoch_time(combined_time):
    t = time.mktime(datetime.datetime.strptime(combined_time,"%Y-%m-%d:%H:%M").timetuple())
    return t

app = Flask(__name__)

@app.route("/", methods=["GET"])
def red():
    return redirect("/home")

@app.route("/home", methods=['POST','GET'])
def index():
    if request.method == 'POST':    
        
        email             = request.form["email"]
        data              = request.form["data"]
        search_date       = request.form["search_date"]
        search_time       = request.form["search_time"]
        epoch_time        = make_epoch_time(str(search_date+":"+search_time))
        delay             = epoch_time - time.time()
        count             = int(request.form["count"])

        autolog(f"epoch time = {epoch_time}  delay={delay}")
        threading.Timer(delay, run_scrapper,(email,data, count,)).start()
        return "<h1>Scrape in progress</h1>"

    else:
        return render_template('index.html')


app.run()

