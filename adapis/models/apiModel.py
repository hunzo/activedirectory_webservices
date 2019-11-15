from flask_restplus import fields, Model


class UsersModels:
    CheckAuthModel = Model(
        'checkauth', {'username': fields.String('Username'), 'password': fields.String('Password')})

    UserinfoModel = Model(
        'getuserinfo', {'username': fields.String('Username Search')})
    AddOUModel = Model(
        'OrganizationUnit', {'ouname': fields.String('Organization Unit name')})

    GroupinfoModel = Model(
        'getgroupinfo', {'groupname': fields.String('Groupname Search')})

    UserIDModel = Model(
        'getuserID', {'id': fields.String('id users in databases')})

    SetUserPasswordModel = Model('setpassword', {'username': fields.String(
        'Username to Change Password'), 'password': fields.String('New password')})

    AddMemberToGroupModel = Model('addmembertogroup', {'username': fields.String(
        'Add User to Groups '), 'groupname': fields.String('Group Name')})

    RemoveMemberFromGroupModel = Model('removememberfromgroup', {'username': fields.String(
        'Remove User from Groups '), 'groupname': fields.String('Group Name')})

    SetUserAttributeModel = Model('setuserattribute', {'username': fields.String(
        'Username to  Set Attributes '), 'attributename': fields.String('Attribute Name'), 'attributevalue': fields.String('Attribute Value')})

    CreateNewGroupModel = Model('createnewgroup', {'groupname': fields.String(
        'New Group Name'), 'description': fields.String('Group Description'), 'groupbasedn': fields.String('New Group will Created in Base OU')})

    CreateNewUsersModel = Model('createnewusers', {'username': fields.String(
        'New User Name'), 'password': fields.String('Password for new users '), 'description': fields.String('New users description '), 'userbasedn': fields.String('New User will Created in Base OU')})

    DeleteUserModel = Model(
        'deleteuser', {'username': fields.String('Delete Users Name')})

    DeleteGroupModel = Model(
        'deletegroup', {'groupname': fields.String('Delete Groups Name')})

    AddBindUserModel = Model('Bind User Model', {'username': fields.String(
        'Username'), 'password': fields.String('password'), 'domain': fields.String('Domain Name'), 'bindou': fields.String('Bind OU'), 'basedn': fields.String('Base DN'), 'serverip': fields.String('AD Server IP Address'), })
