################################################################################
#
# This program is part of the MySQLMon Zenpack for Zenoss.
# Copyright (C) 2009-2012 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""interfaces

describes the form field to the user interface.

$Id: interfaces.py,v 1.3 2012/04/22 22:07:02 egor Exp $"""

__version__ = "$Revision: 1.3 $"[11:-2]

from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t
from ZenPacks.community.RDBMS.interfaces import IDatabaseInfo, IDBSrvInstInfo


class IMySqlDatabaseInfo(IDatabaseInfo):
    """
    Info adapter for MySQL Database components.
    """
    activeTime = schema.Text(title=u"Created", readonly=True, group=u"Details")
    version = schema.Text(title=u"Version", readonly=True, group=u"Details")
    collation = schema.Text(title=u"Collation", readonly=True, group=u"Details")


class IMySqlSrvInstInfo(IDBSrvInstInfo):
    """
    Info adapter for MySQL Server Instance components.
    """
    hostname = schema.Text(title=u"Hostname", readonly=True, group=u"Details")
    port = schema.Text(title=u"Port", readonly=True, group=u"Details")
    version = schema.Text(title=u"Product Version", readonly=True, group=u"Details")
    license = schema.Text(title=u"License Type", readonly=True, group=u"Details")
    have = schema.List(title=u"Instance Properties", readonly=True, group=u"Details")
