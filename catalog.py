from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})

# Bind the above engine to a session.
Session = sessionmaker(bind=engine)

# Create a Session object.
session = Session()

user1 = User(
    name='Chaithra J',
    email='jchaithra@gmail.com',
    picture='https://img.com/sdf'
)

session.add(user1)
session.commit()



#Items for Soccer
category1=Category(user=user1, name="Soccer")
session.add(category1)
session.commit()

item1=Item(user=user1, name="Soccer cleats", description="The Shoes", category=category1)
session.add(item1)
session.commit()

item2=Item(user=user1,name="Jersey", description="The Shirt", category=category1)
session.add(item2)
session.commit()

item3=Item(user=user1, name="Shin Guard", description="The Shin Guard", category=category1)
session.add(item3)
session.commit()

item4=Item(user=user1, name="Socks", description="The Sock", category=category1)
session.add(item4)
session.commit()

#Items for Basketball
category2=Category(user=user1, name="Basketball")
session.add(category2)
session.commit()

item1=Item(user=user1, name="Shoes", description="The Shoes", category=category2)
session.add(item1)
session.commit()

item2=Item(user=user1, name="Jersey", description="The Shirt", category=category2)
session.add(item2)
session.commit()

item3=Item(user=user1, name="Basketball", description="The Ball", category=category2)
session.add(item3)
session.commit()

#Items for Baseball
category3=Category(user=user1, name="Baseball")
session.add(category3)
session.commit()

item1=Item(user=user1, name="Shoes", description="The Shoes", category=category3)
session.add(item1)
session.commit()

item2=Item(user=user1, name="Ball", description="The ball", category=category3)
session.add(item2)
session.commit()

item3=Item(user=user1, name="Bat", description="The bat", category=category3)
session.add(item3)
session.commit()

item4=Item(user=user1, name="Cap", description="The cap", category=category3)
session.add(item4)
session.commit()

#Items for Frisbee
category4=Category(user=user1, name="Frisbee")
session.add(category4)
session.commit()

item1=Item(user=user1, name="Disc", description="The disc", category=category4)
session.add(item1)
session.commit()

#Items for Snowboarding
category5=Category(user=user1, name="Snowboarding")
session.add(category5)
session.commit()

item1=Item(user=user1, name="Snowboard", description="Wooden board", category=category5)
session.add(item1)
session.commit()

#category1 = Category(
#    name='Snowboarding',
#    user=user1
#)

#session.add(category1)
#session.commit()

#item1 = Item(
#    name='Snowboard',
#    description='It is an exciting snowboard. You will feel like in heaven after driving it!',
#    category=category1,
#    user=user1
#)

#session.add(item1)
#session.commit()

#print('Finished populating the database!')


#Items for Rockclimbing
category6=Category(user=user1, name="Rockclimbing")
session.add(category6)
session.commit()

item1=Item(user=user1, name="Shoes", description="Studed Shoes", category=category6)
session.add(item1)
session.commit()

item2=Item(user=user1, name="Gloves", description="Wollen gloves", category=category6)
session.add(item2)
session.commit()

item3=Item(user=user1, name="Rope", description="Long rope", category=category6)
session.add(item3)
session.commit()


print ("Added catalog")
