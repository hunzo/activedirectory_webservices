from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from adapis.models.apiModel import UsersModels as model
from adapis.controller.ConnectAD import ADOperation
from adapis.lib.TokenAuth import token_required, authorizations
import os

adservice_api = Namespace(
    'APIs for ActiveDirectory Services', 
    description='Active Directory Domain ' + os.environ.get('DOMAIN_NAME'), 
    authorizations=authorizations)

Con = ADOperation()


@adservice_api.route('/getadinfo')
class GetActiveDirectoryInformation(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    def get(self):
        """Get Active Directory Informations
        """
        rs = Con.getad_info()
        return jsonify({'result': rs})


@adservice_api.route('/checkauth')
class CheckUserAuth(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.CheckAuthModel)
    def post(self):
        """Check Username and Password Authentications
        """
        r = request.get_json()
        rs = Con.check_auth(r['username'], r['password'])
        return jsonify({'result': rs})


@adservice_api.route('/getgroupinfo')
class GetGroupInfo(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.GroupinfoModel)
    def post(self):
        """Check Group Information
        """
        r = request.get_json()
        rs = Con.get_all_group(r['groupname'])

        return jsonify({'result': rs})


@adservice_api.route('/getgroupname')
class GetGroupName(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.GroupinfoModel)
    def post(self):
        """Check Group Names
        """
        r = request.get_json()
        rs = Con.get_all_group_name(r['groupname'])

        return jsonify({'result': rs})


@adservice_api.route('/getfulluserinfo')
class GetUserInformation(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.UserinfoModel)
    def post(self):
        """Get User Informations
        """
        r = request.get_json()
        rs = Con.get_userinfo(r['username'])

        return jsonify({'result': rs})


@adservice_api.route('/getuserinfo')
class GetUserMiniInformation(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.UserinfoModel)
    def post(self):
        """Get User Informations
        """
        r = request.get_json()
        rs = Con.get_mini_userinfo(r['username'])

        return jsonify({'result': rs})


@adservice_api.route('/setuserpassword')
class SetUserPassword(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.SetUserPasswordModel)
    def put(self):
        """Set user Passwords 
        """
        r = request.get_json()
        rs = Con.set_user_password(r['username'], r['password'])

        return jsonify({'result': rs})


@adservice_api.route('/setuserattribute')
class SetUserAttribute(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.SetUserAttributeModel)
    def put(self):
        """Modified Attributes Users 
        """
        r = request.get_json()
        rs = Con.set_user_attributes(
            r['username'], r['attributename'], r['attributevalue'])

        return jsonify({'result': rs})


@adservice_api.route('/addmembertogroup')
class AddMemberToGrop(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.AddMemberToGroupModel)
    def put(self):
        """Add User to Groups  
        """
        r = request.get_json()
        rs = Con.set_member_togroup(r['username'], r['groupname'])

        return jsonify({'result': rs})


@adservice_api.route('/removememberfromgroup')
class RemoveMemberFromGroup(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.RemoveMemberFromGroupModel)
    def put(self):
        """Remove Users From Group 
        """
        r = request.get_json()
        rs = Con.remove_member_fromgroup(r['username'], r['groupname'])

        return jsonify({'result': rs})


@adservice_api.route('/creategroup')
class CreateGroup(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.CreateNewGroupModel)
    def post(self):
        """Create New Group 
        """
        r = request.get_json()
        rs = Con.create_newgroup(
            r['groupname'], r['description'], r['groupbasedn'])

        return jsonify({'result': rs})


@adservice_api.route('/createuser')
class CreateUser(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.CreateNewUsersModel)
    def post(self):
        """Create New User 
        """
        r = request.get_json()
        rs = Con.create_newusers(r['username'], r['password'],
                                 r['description'], r['userbasedn'])

        return jsonify({'result': rs})


@adservice_api.route('/deletegroup')
class DeleteGroup(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.DeleteGroupModel)
    def delete(self):
        """Delete Group
        """
        r = request.get_json()
        rs = Con.delete_group(r['groupname'])

        return jsonify({'result': rs})


@adservice_api.route('/deleteuser')
class DeleteUser(Resource):
    @adservice_api.doc(security='apikey')
    @token_required
    @adservice_api.expect(model.DeleteUserModel)
    def delete(self):
        """Delete User
        """
        r = request.get_json()
        rs = Con.delete_user(r['username'])

        return jsonify({'result': rs})
