from . import db 

# database model that will be migrated into postgress
class Property(db.Model):
    __tablename__ = 'properties'
    # tables in database

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    num_bedrooms = db.Column(db.String(80))
    num_bathrooms = db.Column(db.String(80))
    location = db.Column(db.String(80))
    price = db.Column(db.String(80))