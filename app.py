from flask import Flask, render_template, redirect, request, abort
from flask_restful import reqparse, abort, Api, Resource

from data.resourses import *
from data.config import secret_api_key

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_api_key
api = Api(app)

# list of classes for bot
api.add_resource(GetListOfClassesResource, '/api/classes_in_paralel') 

# get schedule for today for specific class
api.add_resource(ScheduleResource, '/api/schedule/<clas>&<day>')

# get list of literature categories
api.add_resource(LibraryCategories, '/api/library/literature_categories')

# match books by the name
api.add_resource(BookByName, '/api/library/match_books/<name>')

# get list of books in a category
api.add_resource(BooksInCategory, '/api/library/books_in_category/<category>')


def main():
    app.run()


if __name__ == '__main__':
    main()

