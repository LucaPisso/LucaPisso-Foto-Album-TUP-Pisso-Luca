from . import db

class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    image = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<photo {self.title} {self.description}>"