from bottle import route, post, run, template, redirect, request
import database

database.set_up_database()
@route("/")
def get_index():
    redirect("/owner-list")

@route("/vehicle-list")
def get_vehicles_list():
    items = database.get_vehicles()
    return template("list_vehicle.tpl", vehicles=items)

@route("/vehicle-add")
def get_add_vehicle():
    owners = database.get_owners()
    return template("add_vehicle.tpl", owners=owners)

@post("/vehicle-add")
def post_add_vehicle():
    name = request.forms.get("name")
    description = request.forms.get("description")
    owner = request.forms.get("ownerId")
    database.add_vehicle(name, description, owner)
    redirect("/vehicle-list")    

@route("/vehicle-update/<id>")
def get_update_vehicle(id):
    items = database.get_vehicles(id)
    owners = database.get_owners()
    return template("update_vehicle.tpl", item=items[0], owners=owners)

@post("/vehicle-update")
def post_update_vehicle():
    name = request.forms.get("name")
    description = request.forms.get("description")
    owner = request.forms.get("ownerId")
    id = request.forms.get("id")
    database.update_vehicle(id, name, description, owner)
    redirect("/vehicle-list")    

@route("/vehicle-delete/<id>")
def get_delete(id):
    database.delete_vehicle(id)
    redirect("/vehicle-list")

@route("/owner-list")
def get_owners_list():
    items = database.get_owners()
    return template("list_owner.tpl", owners=items)

@route("/owner-add")
def get_add_owner():
    return template("add_owner.tpl")

@post("/owner-add")
def post_add_owner():
    name = request.forms.get("name")
    location = request.forms.get("location")
    database.add_owner(name, location)
    redirect("/owner-list")    

@route("/owner-update/<id>")
def get_update_owner(id):
    items = database.get_owners(id)
    return template("update_owner.tpl", item=items[0])

@post("/owner-update")
def post_update_owner():
    name = request.forms.get("name")
    location = request.forms.get("location")
    id = request.forms.get("id")
    database.update_owner(id, name, location)
    redirect("/owner-list")    

@route("/owner-delete/<id>")
def get_delete_owner(id):
    database.delete_owner(id)
    redirect("/owner-list")

run(host='localhost', port=8080)