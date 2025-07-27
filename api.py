from flask import Flask, jsonify
from howlongtobeatpy import HowLongToBeat
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # A forma simples e correta com Flask-CORS

@app.route('/howlongtobeat/<string:game_name>')
def get_game_data(game_name):
    try:
        results = HowLongToBeat().search(game_name)
        if results:
            best_match = results[0]
            game_data = {
                "name": best_match.game_name,
                "platforms": best_match.profile_platforms,
                "image_url": best_match.game_image_url,
                "times": {
                    "main_story": best_match.main_story,
                    "main_extra": best_match.main_extra,
                    "completionist": best_match.completionist
                },
                "hltb_url": best_match.game_web_link,
                "search_term": game_name
            }
            return jsonify(game_data)
        else:
            return jsonify({"error": "Jogo não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": "Ocorreu um erro interno", "details": str(e)}), 500

# O bloco if __name__ == '__main__' não é mais necessário para Gunicorn, mas pode deixar
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)