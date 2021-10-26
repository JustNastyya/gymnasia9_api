from data.library_parse import LibraryBD
from data.schedule_parse import ScheduleParser
from flask_restful import reqparse, abort, Resource
from flask import jsonify

# the hole schedule parser

schedule_parser = ScheduleParser()
library_parser = LibraryBD()

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


class LibraryCategories(Resource):
    def get(self):
        return jsonify(library_parser.get_all_categories())


class BooksInCategory(Resource):
    def get(self, category):
        res =  library_parser.get_all_books_in_category(category)
        return jsonify(nice_library_answer(res))


class BookByName(Resource):
    def get(self, name):
        all_books = library_parser.get_all()
        mod_name = [i for i in name.lower().split()]
        res = []
        for book in all_books:  # book = (clas, name)
            if name_comparison(mod_name, book[1]):
                res.append(book)

        return jsonify(nice_library_answer(res))


def name_comparison(mod_name, book_name):
    mod_book_name = [i for i in book_name.lower().split()]
    mod_name = set(mod_name)
    mod_book_name = set(mod_book_name)

    if len(mod_book_name & mod_name) > 0:
        return True
    return False


def nice_library_answer(data):
    res = dict()
    for i in data:
        if i[0] in res.keys():
            res[i[0]].append(i[1])
        else:
            res[i[0]] = [i[1]]
    return res
