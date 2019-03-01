from flask import Flask
from flask import render_template
import formitas
from flask import request
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    formulario = formitas.CommentForm(request.form)
    if request.method == 'POST' and formulario.validate():
        print(formulario.username.data)
        print(formulario.comment.data)
        print(formulario.email.data)
    return render_template("index.html", form = formulario)


if __name__ == "__main__":
    app.run(debug = True, port= 8000)