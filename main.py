from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
        items = ["Python", "Java", "Kotlin", "Go"]
        return render_template('hello.html', items=items)




if __name__ == '__main__':
    app.run()