from flask import Flask,render_template,url_for,request
from database import Data

students = Data.students

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    css_ = url_for('static', filename='styles.css')
    result = ()
    submitted = False

    if request.method == "POST":
        submitted = True

        try:
            registerNumber = int(request.form.get("registerNum"))
            # Return a default 'not found' tuple when missing so template logic works
            result = students.get(registerNumber)
        except (ValueError,TypeError):
            result = None
    
    return render_template('index.html', css_path=css_, result=result, submitted=submitted)

if __name__ == "__main__":
    app.run(debug=True)