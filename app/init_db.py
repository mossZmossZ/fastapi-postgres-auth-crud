from sqlalchemy.orm import Session
from app.models import Base, User, Item
from app.database import engine, SessionLocal
from passlib.hash import bcrypt

def init_db():
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()

    # Create admin user if not exists
    if not db.query(User).filter(User.username == "admin").first():
        admin_user = User(
            username="admin",
            password=bcrypt.hash("admin")
        )
        db.add(admin_user)
        print("[✔] Admin user created.")

    # Insert some mock items if table empty
    if not db.query(Item).first():
        items = [
            Item(name="Item A", description="Mock item A"),
            Item(name="Item B", description="Mock item B"),
            Item(name="Item C", description="Mock item C"),
        ]
        db.add_all(items)
        print(f"[✔] Inserted {len(items)} mock items.")

    db.commit()
    db.close()

if __name__ == "__main__":
    init_db()
