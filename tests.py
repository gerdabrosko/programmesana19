from flask import Flask

app = Flask (__name___)

@app.route("/")
def index ():
    return "Sveiki!"

if __name__== '_main_':
    app.run (port = 5000)
    
print("Sveiki!")