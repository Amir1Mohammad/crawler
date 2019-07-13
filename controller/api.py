# Python imports

# Flask imports
from flask import jsonify
# Project imports
from model.announcement import Announcement
from controller import app
from flask_login import login_required

__Author__ = "Amir Mohammad"


# @login_required
@app.route('/api_1/<int:id>/d1v4r', methods=['GET'])
def get_detail_announcement_from_divar(id):
    return jsonify(Announcement.query.get_or_404(id).to_dict())


@app.route('/api_1/all/d1v4r/<int:page>', methods=['GET'])
def get_announcement_estate_agent(page):

    paginate_obj = Announcement.query.filter_by(owner='شخصی').paginate(1, 3, False).items
    # print(paginate_obj)

    for each in paginate_obj:
        print(each.title)
    return 'hello'
