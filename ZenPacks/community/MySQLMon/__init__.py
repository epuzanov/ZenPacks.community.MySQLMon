
import Globals
import os.path

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

from Products.ZenModel.ZenPack import ZenPackBase

class ZenPack(ZenPackBase):
    """ MySQLMon loader
    """

    packZProperties = [
            ('zMySqlConnectionString', "'MySQLdb',host='${here/manageIp}',port=${here/port},db='information_schema',user='${here/zMySqlUsername}',passwd='${here/zMySqlPassword}'", 'string'),
            ('zMySqlUsername', 'zenoss', 'string'),
            ('zMySqlPassword', '', 'password'),
            ('zMySqlPorts', ['3306'], 'lines'),
            ]

