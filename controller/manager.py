# Python imports
from flask import render_template, url_for, request, flash

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
    ann_obj = 0
    page = request.args.get('page', 1, type=int)
    logs = Log.query.order_by(Log.created_at.desc()).paginate(page, app.config['LOG_PER_PAGE'], False)  # True => 404
    for each in logs.items:
        ann_obj = Announcement.query.get_or_404(each.announcement_id)
    next_url = url_for('retrieve_log', page=logs.next_num) if logs.has_next else None
    prev_url = url_for('retrieve_log', page=logs.prev_num) if logs.has_prev else None
    return render_template("log.html", posts=logs.items, next_url=next_url, prev_url=prev_url, ann_obj=ann_obj)


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
        # test(body, sleep_from, sleep_to)
        # scrape_tehran.apply_async()

    return render_template('basket.html', form=form)


@login_required
@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
