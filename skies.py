from flask import Flask, render_template
import urllib2, json

skies = Flask(__name__);

#retrieves NASA's pic of the day using REST API
@skies.route("/")
def root():
    #retrieve info
    nasa = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=Jpkr0i8IIufXKhweJ0rzE0z6MBlWGxqU5yMl4Tzd")
    #stringify
    snasa = nasa.read()
    #jsonify
    dnasa = json.loads(snasa)
    return render_template("nicepic.html",
                           title = dnasa.get('title'),
                           cred = dnasa.get('copyright'),
                           text = dnasa.get('explanation'),
                           pic = dnasa.get('hdurl'));

@skies.route("/disaster")
def disaster():
    usgs = urllib2.urlopen("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=20&minmagnitude=3")
    susgs = usgs.read()
    dusgs = json.loads(susgs)
    #list of earthquakes is in the key: features
    rawlist = dusgs.get('features')
    #must retrieve relevant info in list of earthquakes
    list = [];
    for e in rawlist:
        #retrieving only the place and value and putting in a dict
        next = {'place': '', 'mag': ''}
        next['place'] = e.get('properties').get('place')
        next['mag'] = e.get('properties').get('mag')
        list.append(next)
    #give the html form a list of dicts with earthquake info in each dict
    return render_template("disaster.html", list = list)


if __name__ == "__main__":
    skies.debug = True;
    skies.run();
