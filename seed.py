from models import Pet, db
from app import app

db.drop_all()
db.create_all()

pet1 = Pet(name="Woofy", species="dog", photo_url="https://images.unsplash.com/photo-1535930749574-1399327ce78f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60")
pet2 = Pet(name="Purry", species="cat", photo_url="https://images.unsplash.com/photo-1548366086-7f1b76106622?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60")
pet3 = Pet(name="Tweety", species="bird", photo_url="https://images.unsplash.com/photo-1518794183325-56eed2af11fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60", age=2, available=False)

db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)

db.session.commit()