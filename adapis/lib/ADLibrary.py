from ldap3 import Server, Connection, ALL_ATTRIBUTES, ALL, SUBTREE, MODIFY_REPLACE, Tls, ALL_OPERATIONAL_ATTRIBUTES
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as addUsersInGroups
from ldap3.extend.microsoft.removeMembersFromGroups import ad_remove_members_from_groups as removeUsersFromGroups
import json
import ssl
import time


class ActiveDirectoryMgmt:
    def check(self):
        print('-'*100)
        print('AD Server : {} \nDomain : {} \nBind User : {}\nBind Password : {}\nAttributes : {}\n'.format(
            self.ad_server_ip, self.ad_domain_name, self.ad_bind_userdn,
            self.ad_bind_pass_userdn, self.ad_attributes_list))
        print('-'*100)

    def __init__(self, ad_server_ip, ad_domain_name, ad_base_dn, ad_bind_userdn, ad_bind_pass_userdn, ad_attributes_list):
        self.ad_server_ip = ad_server_ip
        self.ad_domain_name = ad_domain_name
        self.ad_base_dn = ad_base_dn
        self.ad_bind_userdn = ad_bind_userdn
        self.ad_bind_pass_userdn = ad_bind_pass_userdn
        self.ad_attributes_list = ad_attributes_list

    def ConnectServer(self):
        tls_config = Tls(validate=ssl.CERT_NONE)
        server = Server(self.ad_server_ip, port=636, use_ssl=True,
                        tls=tls_config, get_info=ALL)

        return server

    def BindADServer(self):
        binuser = self.ad_bind_userdn + '@' + self.ad_domain_name

        tls_config = Tls(validate=ssl.CERT_NONE)
        server = Server(self.ad_server_ip, port=636, use_ssl=True,
                        tls=tls_config, get_info=ALL)
        con = Connection(server, user=binuser,
                         password=self.ad_bind_pass_userdn)

        if not con.bind():
            print(con.result)
            return con.result

        return con

    def ad_auth_ldap(self, USER_NAME, USER_PASSWORD):
        user_dn = USER_NAME + '@' + self.ad_domain_name

        s = self.ConnectServer()
        c = Connection(s, user=user_dn, password=USER_PASSWORD)

        if not c.bind():
            print('error in bind : {}', c.result)

        c.unbind()
        r = c.result
        return r

    def search_adusers_information(self, SEARCH_USERS):
        filters = '(&(objectclass=person)(cn=' + SEARCH_USERS + '))'

        # self.check()
        # print(SEARCH_USERS)

        try:
            conn = self.BindADServer()
            conn.start_tls()

            if not conn.bind():
                return 'Bind ERROR {}'.format(conn.result)

            searchParameters = {
                'search_base': self.ad_base_dn,
                'search_filter': filters,
                # 'attributes': self.ad_attributes_list,
                'attributes': ALL_ATTRIBUTES,
                # 'attributes': ALL_OPERATIONAL_ATTRIBUTES,
                'paged_size': 5,
                'paged_cookie': 5,
                'search_scope': SUBTREE
            }
            conn.search(**searchParameters)
            en = conn.entries

        except Exception as e:
            return 'ERROR from search_adusers_information()--->{}'.format(e)

        conn.unbind()

        user_data = []
        for i in en:
            user_entry = json.loads(i.entry_to_json())
            user_data.append(user_entry['attributes'])

        if user_data == []:
            return {'result': 'No user Exists !!!', 'description': 'UserDoesNotExist'}

        return user_data

    def search_adusers_mini_information(self, SEARCH_USERS):
        filters = '(&(objectclass=person)(cn=' + SEARCH_USERS + '))'

        # self.check()
        # print(SEARCH_USERS)

        attributes_list = ['displayname', 'Distinguishedname',
                           'accountexpires', 'userPrincipalName', 'userAccountControl', 'c', 'initials']

        try:
            conn = self.BindADServer()
            conn.start_tls()

            if not conn.bind():
                return 'Bind ERROR {}'.format(conn.result)
            searchParameters = {
                'search_base': self.ad_base_dn,
                'search_filter': filters,
                # 'attributes': self.ad_attributes_list,
                'attributes': attributes_list,
                'paged_size': 5,
                'paged_cookie': 5,
                'search_scope': SUBTREE
            }
            conn.search(**searchParameters)
            en = conn.entries

        except Exception as e:
            return 'ERROR from search_adusers_mini_information()--->{}'.format(e)

        conn.unbind()

        user_data = []
        for i in en:
            user_entry = json.loads(i.entry_to_json())
            user_data.append(user_entry['attributes'])

        return user_data

    def search_group(self, SEARCH_GROUP):
        filters = '(&(objectclass=group)(cn=' + SEARCH_GROUP + '))'

        # self.check()
        # print(SEARCH_USERS)

        attributes_list = ['cn', 'member', 'sAMAccountName', 'managedBy',
                           'displayName', 'distinguishedName', 'whenCreated']

        try:
            conn = self.BindADServer()
            conn.start_tls()

            if not conn.bind():
                return 'Bind ERROR {}'.format(conn.result)

            searchParameters = {
                'search_base': self.ad_base_dn,
                'search_filter': filters,
                # 'attributes': self.ad_attributes_list,
                'attributes': attributes_list,
                'paged_size': 5,
                'paged_cookie': 5,
                'search_scope': SUBTREE
            }
            conn.search(**searchParameters)
            en = conn.entries

        except Exception as e:
            return 'ERROR from search_group()--->{}'.format(e)

        conn.unbind()
        user_data = []
        for i in en:
            user_entry = json.loads(i.entry_to_json())
            user_data.append(user_entry['attributes'])

        return user_data

    def search_group_name(self, SEARCH_GROUP):
        filters = '(&(objectclass=group)(cn=' + SEARCH_GROUP + '))'

        # self.check()
        # print(SEARCH_USERS)

        attributes_list = ['cn', 'sAMAccountName', 'managedBy',
                           'displayName', 'distinguishedName', 'whenCreated']

        try:
            conn = self.BindADServer()
            conn.start_tls()

            if not conn.bind():
                return 'Bind ERROR {}'.format(conn.result)

            searchParameters = {
                'search_base': self.ad_base_dn,
                'search_filter': filters,
                # 'attributes': self.ad_attributes_list,
                'attributes': attributes_list,
                'paged_size': 5,
                'paged_cookie': 5,
                'search_scope': SUBTREE
            }
            conn.search(**searchParameters)
            en = conn.entries

        except Exception as e:
            return 'ERROR from search_group_name()--->{}'.format(e)

        conn.unbind()
        user_data = []
        for i in en:
            user_entry = json.loads(i.entry_to_json())
            user_data.append(user_entry['attributes'])

        return user_data

    def set_user_password(self, username, newpassword):
        try:
            USER_DN = self.__get_ad_users_group_dn('person', username)
        except Exception as e:
            return e
        print(USER_DN)

        try:
            rs = self.__modify_ad_password(USER_DN, newpassword)
        except Exception as e:
            return e

        return rs

    def set_user_attribute(self, username, attributename, attributevalue):
        try:
            USER_DN = self.__get_ad_users_group_dn('person', username)
        except Exception as e:
            return 'error---getdn: {}'.format(str(e))

        print(USER_DN)

        try:
            rs = self.__modify_ad_attributes(
                USER_DN, attributename, attributevalue)
        except Exception as e:
            return 'error---ModAttribute: {}'.format(str(e))

        return rs

    # def search_usersdn_groupdn(self, SERCH_TYPE, SEARCH_NAME):
    #     # SEARCH_TYPE ---> Person, Group

    #     filters = '(&(objectclass=' + SERCH_TYPE + ')(cn=' + SEARCH_NAME + '))'

    #     try:
    #         conn = self.BindADServer()
    #         conn.start_tls()
    #         if not conn.bind():
    #             return 'Bind ERROR {}'.format(conn.result)
    #         searchParameters = {
    #             'search_base': self.ad_base_dn,
    #             'search_filter': filters,
    #             # 'attributes': self.ad_attributes_list,
    #             'attributes': ['distinguishedName'],
    #             'paged_size': 5,
    #             'paged_cookie': 5,
    #             'search_scope': SUBTREE
    #         }
    #         conn.search(**searchParameters)
    #         en = conn.entries

    #     except Exception as e:
    #         return 'error---Search_dn: {}'.format(e)

    #     conn.unbind()

    #     user_data = []
    #     for i in en:
    #         user_entry = json.loads(i.entry_to_json())
    #         user_data.append(user_entry['attributes'])

    #     return user_data

    def add_member_to_group(self, MEMBER_NAME, GROUP_NAME):
        group_dn = self.__get_ad_users_group_dn('group', GROUP_NAME)
        user_dn = self.__get_ad_users_group_dn('person', MEMBER_NAME)
        print(group_dn, user_dn)

        try:
            conn = self.BindADServer()
            conn.start_tls()
            # if not conn.bind():
            #     return 'Bind ERROR {}'.format(conn.result)

            rs = addUsersInGroups(conn, user_dn, group_dn,
                                  raise_error=True, fix=False)
            print(rs, group_dn, user_dn)

        except Exception as e:
            return {'description': 'entryAlreadyExists', 'result': str(e)}

        conn.unbind()

        if rs:
            return {'desctiption': 'success', 'user_dn': user_dn, 'group_dn': group_dn, 'operation': 'add member to group'}

    def remove_member_from_group(self, MEMBER_NAME, GROUP_NAME):
        group_dn = self.__get_ad_users_group_dn('group', GROUP_NAME)
        user_dn = self.__get_ad_users_group_dn('person', MEMBER_NAME)
        print(group_dn, user_dn)

        try:
            conn = self.BindADServer()
            conn.start_tls()

            # if not conn.bind():
            #     return 'Bind ERROR {}'.format(conn.result)

            rs = removeUsersFromGroups(
                conn, user_dn, group_dn, raise_error=True, fix=False)

        except Exception as e:
            return {'description': 'entryNotExists', 'result': str(e)}

        conn.unbind()

        if rs:
            return {'desctiption': 'success', 'user_dn': user_dn, 'group_dn': group_dn, 'operation': 'Remove member from group'}

    def delete_user(self, USER_NAME):
        user_dn = self.__get_ad_users_group_dn('person', USER_NAME)
        # print(user_dn)

        if "SEARCH_ERROR" in user_dn:
            return {'desctiption': 'userNoExists', 'username': USER_NAME, 'errors': user_dn, 'operation': 'delete User'}

        if "NotAllows" in user_dn:
            return {'desctiption': 'notAllowInput', 'username': USER_NAME, 'errors': user_dn, 'operation': 'delete User'}

        try:
            conn = self.BindADServer()
            conn.start_tls()
            conn.delete(user_dn)
        except Exception as e:
            return {'description': 'entryNotExists', 'result': str(e)}

        conn.unbind()

        return {'desctiption': 'success', 'username': USER_NAME, 'userdn': user_dn, 'operation': 'delete User' + USER_NAME}

    def delete_group(self, GROUP_NAME):
        group_dn = self.__get_ad_users_group_dn('group', GROUP_NAME)
        # print(group_dn)

        if "SEARCH" in group_dn:
            return {'desctiption': 'groupNoExists', 'groupname': GROUP_NAME, 'errors': group_dn}

        if "NotAllows" in group_dn:
            return {'desctiption': 'notAllowInput', 'groupname': GROUP_NAME, 'errors': group_dn}

        try:
            conn = self.BindADServer()
            conn.start_tls()
            conn.delete(group_dn)
        except Exception as e:
            return {'description': 'entryNotExists', 'result': str(e)}

        conn.unbind()

        return {'desctiption': 'success', 'groupname': GROUP_NAME, 'groupdn': group_dn, 'operation': 'delete Group' + GROUP_NAME}

    def create_user(self, USER_BASE_DN, NEW_USER, NEW_USER_PASWORD, DESCRIPTION):
        try:
            conn = self.BindADServer()
            conn.start_tls()

            temp_user_dn = 'cn=' + NEW_USER + ',' + USER_BASE_DN

            conn.add(temp_user_dn, 'user', {'givenName': NEW_USER, 'description': "Create Time - " + time.ctime() + " " + DESCRIPTION,
                                            'samaccountname': NEW_USER, 'userPrincipalName': NEW_USER + '@' + self.ad_domain_name, 'c': 'TH'})
            if conn.result['result'] != 0:
                conn.unbind
                return {'desctiption': 'CreateUserErrors', 'username': NEW_USER, 'userdn': temp_user_dn, 'result': conn.result}

            conn.extend.microsoft.modify_password(
                temp_user_dn, NEW_USER_PASWORD)

            if conn.result['result'] != 0:
                conn.delete(temp_user_dn)
                conn.unbind
                return {'desctiption': 'InvalidPasswordPolicy', 'username': NEW_USER, 'userdn': temp_user_dn, 'result_delete': conn.result}

            conn.modify(temp_user_dn, {'userAccountControl': [
                        (MODIFY_REPLACE, ['512'])]})

        except Exception as e:
            return 'Create User Error : {}'.format(e)

        conn.unbind()

        return {'desctiption': 'success', 'username': NEW_USER, 'userdn': temp_user_dn, 'operation': 'create new users'}

    def create_group(self, GROUP_BASE_DN, NEW_GROUP, DESCRIPTION):
        try:
            conn = self.BindADServer()
            conn.start_tls()
            if not conn.bind():
                return 'Bind ERROR {}'.format(conn.result)

            temp_group_dn = 'cn=' + NEW_GROUP + ',' + GROUP_BASE_DN
            print(temp_group_dn)

            conn.add(temp_group_dn, 'group', {
                     'description': DESCRIPTION, 'sAMAccountName': NEW_GROUP, 'displayName': NEW_GROUP})

            if conn.result['result'] != 0:
                conn.unbind()
                return conn.result
            print(conn.result)

        except Exception as e:
            return {'desctiption': 'CreateGroupErrors', 'groupname': NEW_GROUP, 'groupdn': temp_group_dn, 'result': conn.result, 'errormsg': str(e)}

        conn.unbind()
        return {'desctiption': 'success', 'groupname': NEW_GROUP, 'groupdn': temp_group_dn, 'operation': 'create new group', 'result': conn.result, 'GroupDescriptions': DESCRIPTION}

    def __modify_ad_password(self, USER_DN, NEW_PASSWORD):
        try:
            conn = self.BindADServer()
            conn.start_tls()

            if not conn.bind():
                return 'Bind ERROR {}'.format(conn.result)

            conn.extend.microsoft.modify_password(USER_DN, NEW_PASSWORD)
            rs_mod = conn.result

        except Exception as e:
            return 'ERROR from modify_ad_password()--->{}'.format(e)

        conn.unbind()

        return (rs_mod)

    def __get_ad_users_group_dn(self, SERCH_TYPE, SEARCH_OBJ):
        # SEARCH_TYPE ---> Person, Group

        filters = '(&(objectclass=' + SERCH_TYPE + ')(cn=' + SEARCH_OBJ + '))'

        if str(SEARCH_OBJ).find('*') != -1:
            return 'NotAllows * Input'
            # return {'result': 'NoAllows', 'description': 'Not Allows \'*\' Input!!!'}
        else:
            try:
                conn = self.BindADServer()
                conn.start_tls()
                if not conn.bind():
                    return 'Bind ERROR {}'.format(conn.result)

                searchParameters = {
                    'search_base': self.ad_base_dn,
                    'search_filter': filters,
                }

                # conn.search(self.ad_base_dn, FILTERS)
                conn.search(**searchParameters)
                entry = conn.entries[0].entry_to_json()
            except Exception as e:
                return 'error---SearchUser_DN: {}'.format(e)

        conn.unbind()
        obj_dn = json.loads(entry)
        return obj_dn['dn']

    def __modify_ad_attributes(self, USER_DN, ATTRIBUTE_NAME, NEW_VALUE):
        try:
            conn = self.BindADServer()
            conn.start_tls()
            # if not conn.bind():
            #     return 'Bind ERROR {}'.format(conn.result)
            conn.modify(USER_DN, {ATTRIBUTE_NAME: [
                        (MODIFY_REPLACE, [NEW_VALUE])]})
            rs_mod = conn.result

        except Exception as e:
            return {'error': str(e)}

        conn.unbind()
        return rs_mod
