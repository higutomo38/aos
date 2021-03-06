import csv

from shared import LoginBlueprint
from shared import AosApi

token_bp_id_address = LoginBlueprint().blueprint()
token = token_bp_id_address[0]
bp_id = token_bp_id_address[1]
address = token_bp_id_address[2]


class GetHostname(object):

    def __init__(self):
        pass

    def make_hostname_list(self):
        """
        Save hostnames on local CSV file for changing hostname and label.
        """
        with open('hostname_label.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(
                ['ID', 'System_ID', 'Role', 'Hostname', 'New Hostname or Label'])
            for node in AosApi().bp_qe_post(token, bp_id, address,
                        "node('system', name='system', \
                         role=is_in(['leaf', 'spine', 'l2_server', 'l3_server']))")['items']:
                node = node['system']
                writer.writerow([node['id'], node['system_id'], node['role'], node['hostname']])

if __name__ == '__main__':
    GetHostname().make_hostname_list()
