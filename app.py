from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    return jsonify({'reply': f'아직 AI 연결 전이야! 받은 메시지: {user_message}'})

if __name__ == '__main__':
    app.run(debug=True)
