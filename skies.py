from flask import Flask, render_template
import urllib2, json

skies = Flask(__name__);

@skies.route("/")
def root():
    nasa = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=Jpkr0i8IIufXKhweJ0rzE0z6MBlWGxqU5yMl4Tzd");
    snasa = nasa.read()
    dnasa = json.loads(snasa);
    return render_template("nicepic.html",
                           title = dnasa.get('title'),
                           cred = dnasa.get('copyright'),
                           text = dnasa.get('explanation'),
                           pic = dnasa.get('url'));

if __name__ == "__main__":
    skies.debug = True;
    skies.run();
