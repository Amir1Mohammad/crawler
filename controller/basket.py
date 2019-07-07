# Python imports

# Flask imports
from flask_login import login_required
from flask import render_template

# Project imports
from controller import app
from form.option import OptionBazaar

__Author__ = "Amir Mohammad"


@login_required
@app.route('/scrape', methods=['GET', 'POST'])
def find_announcement():
    form = OptionBazaar()
    if form.validate_on_submit():
        print('=====================================')
        print(form.power.data)
    return render_template('basket.html', form=form)
