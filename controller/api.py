# Python imports


# Flask imports
from flask import jsonify
# Project imports
from model.announcement import Announcement
from controller import app, cache
from decorators import token_required

__Author__ = "Amir Mohammad"


@app.route('/api_1/<int:id>/d1v4r', methods=['GET', 'POST'])
@token_required
def get_detail_announcement_from_divar(id):
    return jsonify(jsonify=Announcement.query.get_or_404(id).to_dict())


@app.route('/api_1/all/d1v4r/<int:page>', methods=['GET', 'POST'])
# @cache.cached(timeout=360)
@token_required
def get_announcement_estate_agent(page):
    announcement_obj = Announcement.query.filter_by(owner='شخصی')
    paginate_obj = announcement_obj.paginate(page, app.config['ANNOUNCEMENTS_PER_PAGE'], False).items  # True return 404
    return jsonify(jsonify=[each.to_dict() for each in paginate_obj])
