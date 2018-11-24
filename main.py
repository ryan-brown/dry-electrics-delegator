from flask import render_template
from app import create_app

app = create_app()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
