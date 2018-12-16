import picoweb
from renderer import Renderer
from wifi import Wifi
from machine import Pin

wifi = Wifi()

wifi.connect()
renderer = Renderer('templates')
app = picoweb.WebApp('onAir')
pins = [Pin(18, Pin.OUT), Pin(5, Pin.OUT), Pin(33, Pin.OUT), Pin(25, Pin.OUT)]
state = False
for pin in pins:
    pin.value(0)

@app.route('/')
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite(renderer.render_template('template.html'))

@app.route('/recording')
def recording(req, resp):
    if req.method == 'POST':
        yield from req.read_form_data()
    else:
        yield from resp.awrite('Invalid Method')
    if req.form['on'] == "ON":
        for cpin in pins:
            cpin.value(1)
    else:
        for rpin in pins:
            rpin.value(0)
    headers = {'Location': '/'}
    yield from picoweb.start_response(resp, status=303, headers=headers)

    yield from resp.awrite(renderer.render_template('template.html'))


app.run(debug=-1, host=wifi.getcurrent_ip())
