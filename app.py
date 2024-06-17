from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

hotspots = []

@app.route('/')
def index():
    return render_template('index.html', hotspots=hotspots)

@app.route('/add_hotspot', methods=['POST'])
def add_hotspot():
    data = request.get_json()
    hotspots.append(data)
    return jsonify({'status': 'success', 'data': data})

if __name__ == '__main__':
    app.run(debug=True)
