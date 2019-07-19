# Python imports

from flask import render_template
from flask import request, flash
# Flask imports
from flask_login import login_required

# Project imports
from controller import app
from controller.tasks import my_scraper_divar_task
from form.option import OptionBazaar

__Author__ = "Amir Mohammad"


@app.route('/scrape', methods=['GET', 'POST'])
@login_required
def find_announcement():
    # First turn off any vpn or proxy
    form = OptionBazaar()
    if form.validate_on_submit() and form.power.data:
        flash('Async Task has been started !')
        my_scraper_divar_task()
        # my_scraper_divar_task.apply_async()
    return render_template('basket.html', form=form)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@login_required
@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
