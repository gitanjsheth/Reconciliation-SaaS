from app.db.database import engine, Base
from app.models import user  # Make sure to import all models you want created

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("All tables created successfully!")