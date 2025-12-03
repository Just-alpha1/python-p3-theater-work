from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Role, Audition

# Create engine and session
engine = create_engine('sqlite:///theater.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Test table creation and relationships
print("Testing table creation and relationships...")

# Create a role
role = Role(character_name="Hamlet")
session.add(role)
session.commit()

# Create auditions for the role
audition1 = Audition(actor="Actor1", location="Stage1", phone=1234567890, role_id=role.id)
audition2 = Audition(actor="Actor2", location="Stage2", phone=987654321, role_id=role.id)
session.add_all([audition1, audition2])
session.commit()

# Test relationships
print(f"Role: {role.character_name}")
print(f"Auditions: {[a.actor for a in role.auditions]}")
print(f"Actors: {role.actors()}")
print(f"Locations: {role.locations()}")

# Test methods
print(f"Lead before hiring: {role.lead()}")
audition1.call_back()
session.commit()
print(f"Lead after hiring: {role.lead().actor}")
print(f"Understudy: {role.understudy()}")

audition2.call_back()
session.commit()
print(f"Understudy after second hire: {role.understudy().actor}")

session.close()
print("Testing completed successfully.")
