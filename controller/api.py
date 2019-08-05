# Python imports

# Flask imports
from flask import jsonify, request, abort
# Project imports
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
@token_required
@cache.memoize(timeout=360)
def get_announcement_estate_agent(page):
    # filter word handle on frontend
    announcement_obj = Announcement.query.filter_by(owner='شخصی'). \
        filter(~Announcement.description.contains('مشاور')). \
        order_by(Announcement.created_at.desc())
    paginate_obj = announcement_obj.paginate(page, app.config['ANNOUNCEMENTS_PER_PAGE'], False).items  # True return 404
    return jsonify(jsonify=[each.to_dict() for each in paginate_obj])


@app.route('/api_1/insert/d1v4r', methods=['POST'])
# @token_required
def getting_data_from_localhost():
    try:
        json_parser = request.get_json()
        title = json_parser['title']
        desc = json_parser['description']
        url = json_parser['url']
        phone_number = json_parser['phone_number']
        size_amount = json_parser['size_amount']
        owner = json_parser['owner']
        type_ = json_parser['type']
        rent = json_parser['rent']
        price = json_parser['price']
        place = json_parser['place']
        build_year = json_parser['build_year']
        lat = json_parser['lat']
        long = json_parser['long']
        deposit_amount = json_parser['deposit_amount']
        rooms_num = json_parser['rooms_num']
        market = json_parser['market']
        token = json_parser['token']
        body = json_parser['body']

        announcement_obj = Announcement(title=title, description=desc, url=url, mobile_number=phone_number,
                                        size_amount=size_amount, owner=owner, type=type_, rent=rent, place=place,
                                        build_year=build_year, lat=lat, long=long, deposit_amount=deposit_amount,
                                        rooms_num=rooms_num, market=market, token=token, price=price)

        db.session.add(announcement_obj)
        db.session.commit()
        print('<<<<<<<<', url, '||| Phone number is : {} --- {} '.format(phone_number, body))

        return jsonify({'message': 'ok', "announcement_id": announcement_obj.id}), 201
    except Exception as error:
        print(error)
        return jsonify({'message': error}), 500


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


@app.route('/api_1/search/announcement/<int:page>', methods=['GET', 'POST'])
@token_required
def search_announcement(page):
    """
    {
       "size_amount_start": 100,
       "size_amount_end" : 200,
       "type" : "ارائه",
       "place":"سعادت‌آباد",
       "build_year":1398,
       "rooms_num":2
    }
    """
    kwargs = {"owner": 'شخصی'}
    json_parser = request.get_json()

    type_ = json_parser['type']
    kwargs.update({"type": type_}) if type_ != "null" else type_
    place = json_parser['place']
    kwargs.update({"place": place}) if place != "null" else place
    build_year = json_parser['build_year']
    kwargs.update({"build_year": build_year}) if build_year != 0 else build_year
    rooms_num = json_parser['rooms_num']
    kwargs.update({"rooms_num": rooms_num}) if rooms_num != 0 else rooms_num
    size_amount_start = json_parser['size_amount_start']
    size_amount_start = 1 if size_amount_start == 0 else size_amount_start
    size_amount_end = json_parser['size_amount_end']
    size_amount_end = 50000 if size_amount_end == 0 else size_amount_end

    query_obj = Announcement.query.filter_by(**kwargs). \
        filter(Announcement.size_amount.between(size_amount_start, size_amount_end)). \
        filter(~Announcement.description.contains('مشاور')). \
        order_by(Announcement.created_at.desc()). \
        paginate(page, app.config['ANNOUNCEMENTS_PER_PAGE'], False).items

    return jsonify(jsonify=[query.to_dict() for query in query_obj])


@app.route('/api_1/search/place', methods=['POST'])
# @cache.cached(timeout=360)
def search_place():
    mylist = []
    json_parser = request.get_json()
    place = json_parser['place']
    place_obj = Announcement.query.filter(Announcement.place.startswith(place)).all()
    [mylist.append(each.place) if each.place not in mylist else None for each in place_obj]  # for remove duplicates
    return jsonify(jsonify={"place": mylist}), 200
