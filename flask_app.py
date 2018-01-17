from flask import Flask,redirect,render_template,request,flash,session
from flask_bootstrap import Bootstrap
mongo_user = "python"
mongo_pass = "12345"
mongo_DB="car_models"
from flask_pymongo  import PyMongo
app =Flask(__name__)
app.config['MONGO_DBNAME']= mongo_DB
app.config['MONGO_URI'] = 'mongodb://'+mongo_user+":"+mongo_pass+"@ds255767.mlab.com:55767/car_models"
Bootstrap(app)

with app.app_context():
    mongo = PyMongo(app)

@app.route("/",methods=["GET","POST"])
def index():
    myvar="ghavam"
    return render_template("index.html",myvar=myvar)


# cars = [
#     {
#         "make":"Honda",
#         "models":{}
#     },
#     {},
#     {}
# ]

@app.route("/add",methods=["GET","POST"])
def add_car():
    cars = mongo.db.cars
    cars.insert([
        {"make":{
            "Honda":{
                "models":{
                        "Civic":{"category":"Compact"},
                        "Accord":{"category":"Sedan"},
                        "CR-V":{"category":"SUV"}

                }
            },
            "Volkswagen":{
                "models": {
                    "Jetta":{"category":"Compact"},
                    "Passat":{"category":"Sedan"},
                    "Tiguan":{"category":"SUV"}

                }
            },
            "Ford":{
                "models": {
                    "Focus":{"category":"Compact"},
                    "Taurus":{"category":"Sedan"},
                    "Escape":{"category":"SUV"}
                }
            }
    }
        }])
    return "Collection is added"

# @app.route("/check",methods=["GET"])
# def check_car():
#     cars= mongo.db.cars
#     for car in cars.find():
#         print(car['make'])
#     return "done"

if __name__ =="__main__":
    app.run(debug=True)