from flask import Flask, render_template, url_for, request
from sklearn.externals import joblib

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        regressor = joblib.load("./simple_linear_regression_model.pkl")
        yearsExperience = [[float(dict(request.form)["years_experience"])]] # 2-d array
        prediction = regressor.predict(yearsExperience)
    
    #return render_template("prediction.html", prediction = dict(request.form))
    return render_template("prediction.html", prediction = float(prediction))


if __name__ == "__main__":
    app.run(debug=True)
