# Python imports

from flask import render_template
from flask import request, flash

# Flask imports
from flask_login import login_required

# Project imports
from sqlalchemy import desc

from controller import app
from controller.tasks import scrape_tehran, shutdown_server
from form.crawl_option import OptionBazaar
from model.user import Log
from model.announcement import Announcement

__Author__ = "Amir Mohammad"


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')


@app.route('/log_file/', methods=['GET'])
@login_required
def retrieve_log():
    log_obj = Log.query.order_by(desc(Log.created_at)).all()
    for each in log_obj:
        ann_obj = Announcement.query.get(each.announcement_id)

    return render_template('log.html', log_obj=log_obj, my_file=ann_obj)


@app.route('/scrape', methods=['GET', 'POST'])
@login_required
def crawler_manager():
    # First turn off any vpn or proxy
    form = OptionBazaar()
    if form.validate_on_submit() and form.power.data:
        flash('Async Task has been started !')

        body = form.body.data
        sleep_from = form.sleep_from.data
        sleep_to = form.sleep_to.data
        scrape_tehran(body, sleep_from, sleep_to)
        # scrape_tehran.apply_async()

    return render_template('basket.html', form=form)


@login_required
@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
