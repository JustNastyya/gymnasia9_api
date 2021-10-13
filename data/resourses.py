from data.schedule_parse import ScheduleParser
from flask_restful import reqparse, abort, Resource
from flask import jsonify

# the hole schedule parser

schedule_parser = ScheduleParser()

# for bd if id does not exist
"""
def abort_if_not_found(id):
    session = db_session.create_session()
    info = session.query(News).get(id)
    if not info:
        abort(404, message=f"News {news_id} not found")
"""

class GetListOfClassesResource(Resource):
    def get(self):
        return jsonify(schedule_parser.get_paralel_list())


class ScheduleResource(Resource):
    def get(self, clas, day):
        return jsonify(schedule_parser.get_schedule(clas, day))


class Resourse(Resource):
    def get(self, id):
        # abort_if_not_found(id)
        # session = db_session.create_session()
        # news = session.query(News).get(news_id)
        # return jsonify({'news': news.to_dict(
        #     only=('title', 'content', 'user_id', 'is_private'))})
        return jsonify({
            'some_info': ['info', 'info1', str(id)]
        })
    """
    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(News).get(news_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})
"""

class ListResourse(Resource):
    def get(self, id):
        # abort_if_not_found(id)
        # session = db_session.create_session()
        # news = session.query(News).get(news_id)
        # return jsonify({'news': news.to_dict(
        #     only=('title', 'content', 'user_id', 'is_private'))})
        return jsonify({
            'some_info': ['info', 'info1', str(id)]
        })

class ClassesInParalel(Resource):
    def get(self):
        return jsonify()