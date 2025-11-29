from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/get_similar', methods=['POST'])
def get_similar_books():

    data = request.get_json(silent=True)
    favorite_book = data.get("favorite_book", "").strip()


    
    
    response.raise_for_status()

 
  
    return jsonify({"similar_books": similar_books})


if __name__ == '__main__':
    app.run(debug=True)
