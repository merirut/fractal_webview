import webview

from fractal_webview.flask_app import flask_app

def app():
    webview.create_window('Gosper Curve', flask_app)
    webview.start()
