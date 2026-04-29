from flask import Flask , render_template , request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    print(request.form)
    name=request.form['name']
    email=request.form['email']
    location = request.form['location']
    languages=request.form['language']
    goal=request.form['goal']
    return render_template('result.html',name=name,
        email=email,
        location=location,
        languages=languages,
        goal=goal)

if __name__=="__main__":
    app.run(debug=True,port=5001)
