from gamereview import db


class Game(db.Model):
    # schema for the Category model
    id = db.Column(db.Interger, primary_key=True)
    game_name = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Info(db.Model):
    # schema for the Category model
    id = db.Column(db.Interger, primary_key=True)
