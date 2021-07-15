from flask import Flask, jsonify, request, redirect, make_response
from leer_modelo import predict


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)


nombreParametros = {
    "imagen" : "file1"
}


htmlRTA = {
    "index": """
    <title>clasificador IA</title>
    <h1>Mi primera app para reconocimiento de gatos y perros</h1>
    <form method=post enctype=multipart/form-data>
          <input type="file" name="file1">
          <input type="submit" value="Upload">
    </form>
    """
}

NAME_FILE = "recibido.jpg"


@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if nombreParametros["imagen"] not in request.files:
            return redirect(request.url)
        else:
            ruta_imagen = request.files[ nombreParametros["imagen"] ]
            if ruta_imagen.filename == "":
                return redirect(request.url)

            if ruta_imagen and allowed_file(ruta_imagen.filename):
                ruta_imagen.save(NAME_FILE)

                rta = predict(NAME_FILE)

                return "Image received, it is a " + rta

    return htmlRTA['index']


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1900, debug=True)
