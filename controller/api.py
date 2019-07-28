# Python imports
import json

# Flask imports
from flask import jsonify, request, Response, abort
# Project imports
from controller.sms import SMSAdapter
from model.announcement import Announcement
from model.user import Log
from controller import app, cache, db
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


@app.route('/api_1/insert/d1v4r', methods=['POST'])
@token_required
def getting_data_from_localhost():
    try:
        parsejson = request.get_json()
        title = parsejson['title']
        desc = parsejson['description']
        url = parsejson['url']
        phone_number = parsejson['phone_number']
        size_amount = parsejson['size_amount']
        owner = parsejson['owner']
        type_ = parsejson['type']
        rent = parsejson['rent']
        place = parsejson['place']
        build_year = parsejson['build_year']
        lat = parsejson['lat']
        long = parsejson['long']
        deposit_amount = parsejson['deposit_amount']
        rooms_num = parsejson['rooms_num']
        market = parsejson['market']
        token = parsejson['token']

        announcement_obj = Announcement(title=title, description=desc, url=url, mobile_number=phone_number,
                                        size_amount=size_amount, owner=owner, type=type_, rent=rent, place=place,
                                        build_year=build_year, lat=lat, long=long, deposit_amount=deposit_amount,
                                        rooms_num=rooms_num, market=market, token=token)

        db.session.add(announcement_obj)
        db.session.commit()
        print('<<<<<<<<', url, '||| Phone number is : {}'.format(phone_number))

        return jsonify({'message': 'ok', "ann_id": announcement_obj.id}), 201
    except:
        pass


@app.route('/api_1/enable/<int:ann_id>/d1v4r', methods=['GET'])
@token_required
def enable_is_seen(ann_id):
    try:
        announcement_obj = Announcement.query.get_or_404(ann_id)
        log_obj = Log(announcement_id=announcement_obj.id, is_seen=True)
        db.session.add(log_obj)
        db.session.commit()
        return jsonify({'message': 'ok'}), 200

    except:
        abort(500)


@app.route('/api_1/submit/<int:ann_id>/d1v4r', methods=['GET'])
@token_required
def enable_is_submit(ann_id):
    try:
        announcement_obj = Announcement.query.get_or_404(ann_id)
        log_obj = Log(announcement_id=announcement_obj.id, is_seen=True, is_submit=True)
        db.session.add(log_obj)
        db.session.commit()
        return jsonify({'message': 'ok'}), 200

    except:
        abort(500)


@app.route('/api_1/search', methods=['GET', 'POST'])
# @token_required
def search_announcement():
    announcement_obj = Announcement.query.all()

    return jsonify(jsonify=[each.to_dict() for each in announcement_obj])
