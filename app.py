from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    items = request.form.getlist('items')
    prices = {
        'butter chicken': 350,
        'pannier tikka': 250,
        'fried rice': 200,
        'hakka noodles': 200,
        'panner handi': 300,
        'choole bhature': 100,
        'manchurian': 90,
        'vegetable soup': 150,
        'pizza': 350,
        'pasta': 150
    }
    total = sum(prices.get(item, 0) for item in items)
    return render_template('order.html', items=items, total=total)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
