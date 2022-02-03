from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

user_put_args = parser.copy()
user_put_args.add_argument("nama", type=str, help="nama user", required=True)
user_put_args.add_argument("umur", type=int, help="umur user", required=True)
user_put_args.add_argument("hp", type=int, help="no hp user", required=True)

role_put_args = parser.copy()
role_put_args.add_argument("job", type=str, help="role job", required=True)
role_put_args.add_argument("ket", type=int, help="ket role", required=True)

userss = {}
roles = {}


def abort_if_user_id_doesnt_exist(user_id):
    if user_id not in userss:
        abort(404, message="User id is not valid ...")


def abort_if_user_id_exist(user_id):
    if user_id in userss:
        abort(409, message="User id already exist with that ID ...")


def abort_if_role_id_doesnt_exist(role_id):
    if role_id not in userss:
        abort(404, message="Role id is not valid ...")


def abort_if_role_id_exist(role_id):
    if role_id in userss:
        abort(409, message="Role id already exist with that ID ...")


class Users(Resource):
    def get(self, user_id):
        abort_if_user_id_doesnt_exist(user_id)
        return userss[user_id]

    def post(self, user_id):
        abort_if_user_id_exist(user_id)
        args = user_put_args.parse_args()
        userss[user_id] = args
        return userss[user_id], 201

    def put(self, user_id):
        abort_if_user_id_doesnt_exist(user_id)
        args = user_put_args.parse_args()
        userss[user_id] = args
        return userss[user_id], 201

    def delete(self, user_id):
        del userss[user_id]
        return {"message": "success delete"}, 201


class Roles(Resource):
    def get(self, role_id):
        abort_if_role_id_doesnt_exist(role_id)
        return roles[role_id]

    def post(self, role_id):
        abort_if_role_id_exist(role_id)
        args = role_put_args.ArgumentParser()
        roles[role_id] = args
        return roles[role_id], 201

    def put(self, role_id):
        abort_if_role_id_doesnt_exist(role_id)
        args = role_put_args.parse_args()
        roles[role_id] = args
        return roles[role_id], 201

    def delete(self, role_id):
        del roles[role_id]
        return {"message": "success delete"}, 201


class Test(Resource):
    def get(self):
        return {"pesan": "success delete"}, 201


api.add_resource(Users, "/user/<int:user_id>")
api.add_resource(Roles, "/role/<int:role_id>")
api.add_resource(Test, "/test")

if __name__ == "__main__":
    app.run(debug=True)
