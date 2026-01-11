from flask import Flask, request, jsonify
from langdetect import detect_langs

app = Flask(__name__)

@app.route('/lg', methods=['GET'])
def detect_language():
    print('detect methode betreten')
    text = request.args.get('id', '')
    print('text übergeben')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    try:
        print('text received')
        result = detect_langs(text)  # Ueberpruefung des
        print('result received')
        if not result:
            return jsonify({'error': 'Could not detect language.'}), 400

        best = result[0]  # bestes Ergebnis uebernehmen
        prob = best.prob * 100  # Wahrscheinlichkeit in % errechnen
        short = best.lang  # Iso639-Abkuerzung der Sprache
        is_reliable = best.prob > 0.5  # Ergebnis ist bei >50% vertrauenswuerdig
        #long = languages.get(part1=short)  # Sprache auf Basis des ISo639-Codes ermitteln

        return jsonify({'short': short, 'reliable': is_reliable, 'prob': prob })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=5000)
