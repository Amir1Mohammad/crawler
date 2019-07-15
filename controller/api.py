# Python imports

# Flask imports
from flask import jsonify, make_response
# Project imports
from model.announcement import Announcement
from controller import app
from config import Config
from flask_login import login_required

__Author__ = "Amir Mohammad"


# @login_required
@app.route('/api_1/<int:id>/d1v4r', methods=['GET'])
def get_detail_announcement_from_divar(id):
    return jsonify(Announcement.query.get_or_404(id).to_dict())


@app.route('/api_1/all/d1v4r/<int:page>', methods=['GET'])
def get_announcement_estate_agent(page):
    listme = []
    announcement_obj = Announcement.query.filter_by(owner='شخصی')
    paginate_obj = announcement_obj.paginate(page, app.config['ANNOUNCEMENTS_PER_PAGE'], False).items  # True return 404

    for each in paginate_obj:
        listme.append({
            'id': each.id,
            'title': each.title,
            'url': each.url,
            'description': each.description,
            'mobile_number': each.mobile_number,
            'size_amount': each.size_amount,
            'type': each.type,
            'rooms_num': each.rooms_num,
            'build_year': each.build_year,
            'owner': each.owner,
        })
    return jsonify(jsonify=listme), 200
