from peewee import *

db = SqliteDatabase('supermarket.db')
db.connect()

class Owner(Model):
    name = CharField()
    location = CharField()
    class Meta:
        database = db

class Vehicle(Model):
    name = CharField()
    description = CharField()
    owner = ForeignKeyField(Owner, backref='vehicles', null=True)
    class Meta:
        database = db 

def set_up_database():
    db.drop_tables([Owner, Vehicle], safe=True)
    db.create_tables([Owner, Vehicle])

def get_owners(id=None):
    if id==None:
        owners = Owner.select()
    else:
        owners = Owner.select().where(Owner.id == id)
    owners = [
        {
            'id': owner.id,
            'name': owner.name,
            'location': owner.location

        }
        for owner in owners
    ]
    return owners

def add_owner(name, location):
    item = Owner(name=name, location=location)
    item.save()

def update_owner(id, name, location):
    item = Owner.select().where(Owner.id == id).get()
    item.name = name
    item.location = location
    item.save()

def delete_owner(id):
    item = Owner.select().where(Owner.id == id).get()
    item.delete_instance()

def get_vehicles(id=None):
    if id==None:
        vehicles = Vehicle.select()
    else:
        vehicles = Vehicle.select().where(Vehicle.id == id)
    vehicles = [
        {
            'id': vehicle.id,
            'name': vehicle.name,
            'description': vehicle.description,
            'owner_name': vehicle.owner.name

        }
        for vehicle in vehicles
    ]
    return vehicles

def add_vehicle(name, description, owner):
    item = Vehicle(name=name, description=description, owner=owner)
    item.save()

def update_vehicle(id, name, desc, owner):
    item = Vehicle.select().where(Vehicle.id == id).get()
    item.name = name
    item.description = desc
    item.owner = owner
    item.save()

def delete_vehicle(id):
    item = Vehicle.select().where(Vehicle.id == id).get()
    item.delete_instance()

