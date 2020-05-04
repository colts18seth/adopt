from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to databse."""
    
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ Pet Model """

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                               primary_key=True,
                               autoincrement=True)
    name = db.Column(db.String(20),
                                    nullable=False)
    species = db.Column(db.String(20),
                                        nullable=False)
    photo_url = db.Column(db.String,
                                            nullable=True)
    age = db.Column(db.Integer,
                                 nullable=True)
    notes = db.Column(db.String,
                                    nullable=True)
    available = db.Column(db.Boolean,
                                          nullable=False,
                                          default=True)

    def __repr__(self):
        """Show pet info"""
        p = self
        return f"<Pet {p.id} {p.name} ({p.species})>"