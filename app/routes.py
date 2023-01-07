from app import app
from app.eventing import CustomEvents
from flask import request,render_template

EventInstance = CustomEvents()

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        EventInstance.on('click', 'Hello')
        EventInstance.on('click','There!')
        EventInstance.trigger('click')
        EventInstance.off('click')
        return render_template('index.html')
    return render_template('index.html')