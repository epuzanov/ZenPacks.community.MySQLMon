################################################################################
#
# This program is part of the MySQLMon Zenpack for Zenoss.
# Copyright (C) 2009-2012 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""info.py

Representation of Databases.

$Id: info.py,v 1.1 2012/04/22 22:04:12 egor Exp $"""

__version__ = "$Revision: 1.1 $"[11:-2]

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from ZenPacks.community.RDBMS.info import DatabaseInfo, DBSrvInstInfo
from ZenPacks.community.MySQLMon import interfaces


class MySqlDatabaseInfo(DatabaseInfo):
    implements(interfaces.IMySqlDatabaseInfo)

    version = ProxyProperty("version")
    collation = ProxyProperty("collation")


class MySqlSrvInstInfo(DBSrvInstInfo):
    implements(interfaces.IMySqlSrvInstInfo)

    hostname = ProxyProperty("hostname")
    port = ProxyProperty("port")
    license = ProxyProperty("license")
    version = ProxyProperty("version")
    have = ProxyProperty("have")
