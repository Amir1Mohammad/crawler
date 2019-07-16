# Python imports


# Flask imports
from flask import jsonify
# Project imports
from model.announcement import Announcement
from controller import app, cache


__Author__ = "Amir Mohammad"


# @login_required
@app.route('/api_1/<int:id>/d1v4r', methods=['GET'])
def get_detail_announcement_from_divar(id):
    return jsonify(jsonify=Announcement.query.get_or_404(id).to_dict())


@app.route('/api_1/all/d1v4r/<int:page>', methods=['GET'])
@cache.cached(timeout=360)
def get_announcement_estate_agent(page):
    announcement_obj = Announcement.query.filter_by(owner='شخصی')
    paginate_obj = announcement_obj.paginate(page, app.config['ANNOUNCEMENTS_PER_PAGE'], False).items  # True return 404
    return jsonify(jsonify=[each.to_dict() for each in paginate_obj])
