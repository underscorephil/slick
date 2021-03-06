from flask import Blueprint

blueprint = Blueprint('network_module', __name__, template_folder='templates',
                      url_prefix='/network')

from slick import app
from . import views, widgets

submenu = [
    ('network_module.subnet_index', 'List Subnets'),
    ('network_module.vlan_index', 'List VLANs'),
]
app.add_menu('left', submenu, 'Networking', 3)

for widget in widgets.get_widgets():
    app.add_widget(widget)

# Subnet Cancel
blueprint.add_url_rule('/subnet/cancel/<int:subnet_id>',
                       view_func=views.subnet_cancel)

# Subnet Create
blueprint.add_url_rule('/subnet/create/<int:vlan_id>',
                       view_func=views.subnet_create, methods=['GET', 'POST'])

# Subnet List
blueprint.add_url_rule('/subnet', view_func=views.subnet_index)

# Subnet View
blueprint.add_url_rule('/subnet/view/<int:subnet_id>',
                       view_func=views.subnet_view)

# VLAN List
blueprint.add_url_rule('/vlan', view_func=views.vlan_index)

# VLAN View
blueprint.add_url_rule('/vlan/view/<int:vlan_id>',
                       view_func=views.vlan_view)
