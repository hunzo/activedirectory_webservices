from adapis.lib.ADLibrary import ActiveDirectoryMgmt
from pprint import pprint
import os


attributes_list = ['CN', 'Distinguishedname', 'displayname', 'mail', 'department', 'optionalemail', 'samaccountname',
                   'lastlogontimestamp', 'info', 'pwdlastset', 'accountexpires', 'accountexpires', 'userPrincipalName',
                   'extensionattribute1', 'extensionattribute2', 'extensionattribute3', 'extensionattribute4',
                   'extensionattribute5', 'extensionattribute6', 'extensionattribute7', 'extensionattribute8',
                   'extensionattribute9', 'extensionattribute10', 'extensionattribute11', 'extensionattribute12',
                   'extensionattribute13', 'extensionattribute14', 'extensionattribute15', 'memberof', 'title',
                   'objectclass', 'userAccountControl', 'description', 'c', 'initials']


DOMAIN_NAME = os.environ.get('DOMAIN_NAME')
BASE_DN = os.environ.get('BASE_DN')
BIND_USER = os.environ.get('BIND_USER')
BIND_PASSWORD = os.environ.get('BIND_PASSWORD')
AD_SERVER = os.environ.get('AD_SERVER')


class ADOperation:

    ConnectActiveDirectory = ActiveDirectoryMgmt(
        AD_SERVER, DOMAIN_NAME, BASE_DN, BIND_USER, BIND_PASSWORD, attributes_list)

    # def __init__(self, username, password, domain, basedn, bindou):
    #     self.username = username
    #     self.password = password
    #     self.domain = domain
    #     self.bindou = bindou
    #     self.basedn = basedn

    def getad_info(self):
        info = {}
        info['attributelist'] = attributes_list
        info['domain'] = os.environ.get('DOMAIN_NAME')
        info['basedn'] = os.environ.get('BASE_DN')
        info['serverip'] = os.environ.get('AD_SERVER')

        return info

    def get_bind_data(self):
        userInfo = {
            'info': '123'
        }
        return userInfo

    def check_auth(self, username, password):
        check = self.ConnectActiveDirectory.ad_auth_ldap(username, password)
        # print('-'*100)
        # print(check)

        return check

    def get_userinfo(self, username):
        try:
            rs = self.ConnectActiveDirectory.search_adusers_information(
                username)
        except Exception as e:
            return str(e)
        data = []
        for i in range(0, len(rs)):
            temp = {}
            try:
                for k, v in rs[i].items():
                    temp[k.lower()] = v
                data.append(temp)
            except Exception as e:
                ret = {
                    'result': 'No user Exists !!!',
                    'description': 'UserDoesNotExist',
                    'error': str(e)
                }
                return ret
        pprint(data)
        return data

    def get_mini_userinfo(self, username):

        try:
            rs = self.ConnectActiveDirectory.search_adusers_mini_information(
                username)
        except Exception as e:
            return str(e)

        if len(rs) == 0:
            ret = {
                'result': 'No user Exists !!!',
                'description': 'UserDoesNotExist',
            }
            return ret

        data = []
        for i in range(0, len(rs)):
            temp = {}
            for k, v in rs[i].items():
                temp[k.lower()] = v
            data.append(temp)
        pprint(data)
        return data

    def get_all_group(self, groupname):
        try:
            rs = self.ConnectActiveDirectory.search_group(groupname)
        except Exception as e:
            return str(e)

        if len(rs) == 0:
            ret = {
                'result': 'No user Exists !!!',
                'description': 'UserDoesNotExist',
            }
            return ret

        data = []
        for i in range(0, len(rs)):
            temp = {}
            for k, v in rs[i].items():
                temp[k.lower()] = v
            data.append(temp)
        pprint(data)
        return data

    def get_all_group_name(self, groupname):
        try:
            rs = self.ConnectActiveDirectory.search_group_name(groupname)
        except Exception as e:
            return str(e)

        if len(rs) == 0:
            ret = {
                'result': 'No user Exists !!!',
                'description': 'UserDoesNotExist',
            }
            return ret

        data = []
        for i in range(0, len(rs)):
            temp = {}
            for k, v in rs[i].items():
                temp[k.lower()] = v
            data.append(temp)
        pprint(data)
        return data

    def set_user_password(self, username, newpassword):
        try:
            rs = self.ConnectActiveDirectory.set_user_password(
                username, newpassword)
        except Exception as e:
            return str(e)
        return rs

    def set_member_togroup(self, username, groupname):

        try:
            rs = self.ConnectActiveDirectory.add_member_to_group(
                username, groupname)
        except Exception as e:
            return str(e)
        print(rs)

        return rs

    def set_user_attributes(self, username, attributename, attributevalue):
        try:
            rs = self.ConnectActiveDirectory.set_user_attribute(
                username, attributename, attributevalue)
        except Exception as e:
            return str(e)
        return rs

    def remove_member_fromgroup(self, username, groupname):
        try:
            rs = self.ConnectActiveDirectory.remove_member_from_group(
                username, groupname)
        except Exception as e:
            return str(e)
        return rs

    def create_newgroup(self, newgroupname, description, group_base_dn):
        GROUP_BASE_DN = group_base_dn
        try:
            rs = self.ConnectActiveDirectory.create_group(
                GROUP_BASE_DN, newgroupname, description)
        except Exception as e:
            return str(e)
        return rs

    def create_newusers(self, newusername, newpassword, description, user_base_dn):
        USER_BASE_DN = user_base_dn
        try:
            rs = self.ConnectActiveDirectory.create_user(
                USER_BASE_DN, newusername, newpassword, description)
        except Exception as e:
            return str(e)

        return rs

    def delete_group(self, groupname):
        try:
            rs = self.ConnectActiveDirectory.delete_group(groupname)
        except Exception as e:
            return str(e)

        return rs

    def delete_user(self, username):
        try:
            rs = self.ConnectActiveDirectory.delete_user(username)
        except Exception as e:
            return str(e)

        return rs
