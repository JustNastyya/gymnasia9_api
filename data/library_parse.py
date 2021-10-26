import sqlite3


class LibraryBD:
    def __init__(self):
        try:
            self.con = sqlite3.connect("bd\\library.db", check_same_thread=False)
        except Exception as e:  # the test is on
            self.con = sqlite3.connect("D:\\school_helper\\new\\db\\library.db", check_same_thread=False)
        self.cur = self.con.cursor()
        self.check_if_table_exists()
    
    def check_if_table_exists(self):
        # for heroku. i guess it deletes bd every time
        try:
            result = self.cur.execute(f"""SELECT Clas FROM books""").fetchone()
        except Exception:
            print('\n\n **Sure. Heroku is fucked** \n\n')
    
    def get_all_categories(self):
        result = self.cur.execute(f"""SELECT category_name from categories""").fetchall()
        result = [i[0] for i in result]
        return result

    def get_all_books_in_category(self, category):
        category = category.lower()
        result = self.cur.execute(f"""SELECT clas, name FROM books
                    WHERE category IN (
                        SELECT id FROM categories 
                            WHERE category_name = '{category}' 
                    )""").fetchall()
        return result
    
    def get_all(self):
        result = self.cur.execute(f"""SELECT clas, name FROM books""").fetchall()
        return result
    
    def __del__(self):
        self.con.close()


def tests():
    # better be run in main.py
    library = LibraryBD()
    from pprint import pprint
    pprint(library.get_all_books_in_category('Математика'))
    print()
    pprint(library.get_all())
    print()
    pprint(library.get_all_categories())


if __name__ == '__main__':
    tests()