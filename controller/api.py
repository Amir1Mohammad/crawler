# Python imports

# Flask imports
from flask import jsonify
# Project imports
from model.announcement import Announcement
from controller import app
from flask_login import login_required

__Author__ = "Amir Mohammad"


@app.route('/api_1/<int:id>/d1v4r', methods=['GET'])
@login_required
def get_detail_announcement_from_divar(id):
    return jsonify(Announcement.query.get_or_404(id).to_dict())