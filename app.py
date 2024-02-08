from flask import Flask, jsonify, request
from observer import battle_subject, PlayerObserver

app = Flask(__name__)

@app.route('/battle/<result>', methods=['POST'])
def finish_battle(result):
    battle_subject.finish_battle(result)
    return jsonify({"message": "Batalha finalizada. Observadores notificados."})

@app.route('/register/<player_name>', methods=['POST'])
def register_observer(player_name):
    observer = PlayerObserver(player_name)
    battle_subject.add_observer(observer)
    return jsonify({"message": f"Jogador {player_name} registrado como observador."})

@app.route('/info', methods=['GET'])
def get_info():
    battle_result = battle_subject.get_last_battle_result()
    observers = [observer.name for observer in battle_subject._observers]
    return jsonify({"battle_result": battle_result, "observers": observers})

if __name__ == '__main__':
    app.run(debug=True)
