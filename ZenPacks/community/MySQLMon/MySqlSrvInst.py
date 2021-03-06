################################################################################
#
# This program is part of the MySQLMon Zenpack for Zenoss.
# Copyright (C) 2009-2012 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""MySqlSrvInst

MySqlSrvInst is a SrvInst

$Id: MySqlSrvInst.py,v 1.1 2012/04/22 21:42:59 egor Exp $"""

__version__ = "$Revision: 1.1 $"[11:-2]

from Globals import InitializeClass
from Products.ZenModel.ZenossSecurity import *
from ZenPacks.community.RDBMS.DBSrvInst import DBSrvInst


class MySqlSrvInst(DBSrvInst):
    """
    MySQL SrvInst object
    """

    ZENPACKID = 'ZenPacks.community.MySQLMon'

    hostname = ''
    port = 0
    version = ''
    license = ''
    have = []


    _properties = DBSrvInst._properties + (
        {'id':'hostname', 'type':'string', 'mode':'w'},
        {'id':'port', 'type':'int', 'mode':'w'},
        {'id':'version', 'type':'string', 'mode':'w'},
        {'id':'license', 'type':'string', 'mode':'w'},
        {'id':'have', 'type':'lines', 'mode':'w'},
        )


    factory_type_information = (
        {
            'id'             : 'MySqlSrvInst',
            'meta_type'      : 'MySqlSrvInst',
            'description'    : """Arbitrary device grouping class""",
            'icon'           : 'FileSystem_icon.gif',
            'product'        : 'MySQLMon',
            'factory'        : 'manage_addDBSrvInst',
            'immediate_view' : 'viewMySqlSrvInst',
            'actions'        :
            (
                { 'id'            : 'status'
                , 'name'          : 'Status'
                , 'action'        : 'viewMySqlSrvInst'
                , 'permissions'   : (ZEN_VIEW,)
                },
                { 'id'            : 'databases'
                , 'name'          : 'Databases'
                , 'action'        : 'viewDBSrvInstDatabases'
                , 'permissions'   : (ZEN_VIEW,)
                },
                { 'id'            : 'events'
                , 'name'          : 'Events'
                , 'action'        : 'viewEvents'
                , 'permissions'   : (ZEN_VIEW,)
                },
                { 'id'            : 'perfConf'
                , 'name'          : 'Template'
                , 'action'        : 'objTemplates'
                , 'permissions'   : (ZEN_CHANGE_DEVICE,)
                },
                { 'id'            : 'viewHistory'
                , 'name'          : 'Modifications'
                , 'action'        : 'viewHistory'
                , 'permissions'   : (ZEN_VIEW_MODIFICATIONS,)
                },
            )
          },
        )

InitializeClass(MySqlSrvInst)
