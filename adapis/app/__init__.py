from flask import Blueprint
from flask_restplus import Api
from adapis.app.nsadapis import adservice_api
from adapis.models.apiModel import UsersModels
import os

bp = Blueprint('bp', __name__)

api = Api(bp, title='Active Directory Web Services',
        version='0.2', 
        description=
        'APIs ' + os.environ.get('DOMAIN_NAME') + '\nauthor : Surapong Naowasate \ndate : 2019-10-25 \nversion : 0.2')

api.models[UsersModels.CheckAuthModel.name] = UsersModels.CheckAuthModel
api.models[UsersModels.UserinfoModel.name] = UsersModels.UserinfoModel
api.models[UsersModels.SetUserPasswordModel.name] = UsersModels.SetUserPasswordModel
api.models[UsersModels.SetUserAttributeModel.name] = UsersModels.SetUserAttributeModel
api.models[UsersModels.AddMemberToGroupModel.name] = UsersModels.AddMemberToGroupModel
api.models[UsersModels.RemoveMemberFromGroupModel.name] = UsersModels.RemoveMemberFromGroupModel
api.models[UsersModels.CreateNewGroupModel.name] = UsersModels.CreateNewGroupModel
api.models[UsersModels.CreateNewUsersModel.name] = UsersModels.CreateNewUsersModel
api.models[UsersModels.DeleteUserModel.name] = UsersModels.DeleteUserModel
api.models[UsersModels.DeleteGroupModel.name] = UsersModels.DeleteGroupModel
api.models[UsersModels.AddBindUserModel.name] = UsersModels.AddBindUserModel
api.models[UsersModels.UserIDModel.name] = UsersModels.UserIDModel
api.models[UsersModels.GroupinfoModel.name] = UsersModels.GroupinfoModel
api.models[UsersModels.AddOUModel.name] = UsersModels.AddOUModel


api.add_namespace(adservice_api, path='/admgmt')
