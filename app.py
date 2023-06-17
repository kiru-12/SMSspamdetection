from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def spam_detection():
    
    model = pickle.load(open('spammodel.pkl', 'rb'))
    vec = pickle.load(open('vectorizer.pkl', 'rb'))
    
    if request.method == 'POST':
        user_input = request.form['text']
        t1 = [user_input]
        inp = vec.transform(t1)
        res = model.predict(inp)
        t2 = ''
        if res == [1]:
            t2 = 'Yes'
        else:
            t2 = 'No'
            
        return render_template('index.html', output=t2)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
