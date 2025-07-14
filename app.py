from flask import Flask, render_template, request
import filma

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    film = None
    gabim = None

    if request.method == 'POST':
        emri = request.form.get('film')
        if emri:
            data = filma.merr_informacion_per_film_me_emri(emri)
            if data and 'Title' in data:
                film = data
            else:
                gabim = "Filmi nuk u gjet. Provo përsëri."
        else:
            gabim = "Ju lutem shkruani emrin e filmit."

    return render_template('index.html', film=film, gabim=gabim)

if __name__ == '__main__':
    app.run(debug=True)
