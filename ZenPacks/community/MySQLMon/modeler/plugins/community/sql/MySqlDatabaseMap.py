################################################################################
#
# This program is part of the MySQLMon Zenpack for Zenoss.
# Copyright (C) 2009-2012 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""MySqlDatabaseMap.py

MySqlDatabaseMap maps the MySQL Databases table to Database objects

$Id: MySqlDatabaseMap.py,v 1.6 2012/04/23 19:19:54 egor Exp $"""

__version__ = "$Revision: 1.6 $"[11:-2]

from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.DataCollector.plugins.DataMaps import MultiArgs
from ZenPacks.community.SQLDataSource.SQLPlugin import SQLPlugin

class MySqlDatabaseMap(ZenPackPersistence, SQLPlugin):


    ZENPACKID = 'ZenPacks.community.MySQLMon'

    maptype = "DatabaseMap"
    compname = "os"
    relname = "softwaredbsrvinstances"
    modname = "ZenPacks.community.MySQLMon.MySqlSrvInst"
    deviceProperties = SQLPlugin.deviceProperties + ('zMySqlUsername',
                                                    'zMySqlPassword',
                                                    'zMySqlConnectionString',
                                                    'zMySqlPorts',
                                                    )


    def queries(self, device):
        tasks = {}
        connectionString = getattr(device, 'zMySqlConnectionString', '') or \
            "'MySQLdb',host='${here/manageIp}',port=${here/port},db='information_schema',user='${here/zMySqlUsername}',passwd='${here/zMySqlPassword}'"
        ports = getattr(device,'zMySqlPorts','') or '3306'
        if type(ports) is str:
            ports = [ports]
        for inst, port in enumerate(ports):
            setattr(device, 'port', int(port))
            cs = self.prepareCS(device, connectionString)
            tasks['si_%s'%inst] = (
                "SHOW VARIABLES",
                None,
                cs,
                {
                    'hostname':'hostname',
                    'port':'port',
                    'license':'license',
                    'version':'version',
                    'version_compile_machine':'setProductKey',
                })
            tasks['vr_%s'%inst] = (
                "SHOW VARIABLES WHERE Variable_name like 'have_%' AND Value='YES'",
                None,
                cs,
                {
                    'Variable_name':'have',
                })
            tasks['db_%s'%inst] = (
                """SELECT table_schema,
                          engine,
                          MIN(create_time) as created,
                          version,
                          MIN(table_collation) as collation,
                          '%s' as instance
                   FROM TABLES
                   GROUP BY table_schema"""%inst,
                None,
                cs,
                {
                    'table_schema':'dbname',
                    'engine':'type',
                    'created':'activeTime',
                    'version':'version',
                    'collation':'collation',
                    'instance':'setDBSrvInst',
                })
        return tasks


    def process(self, device, results, log):
        log.info('processing %s for device %s', self.name(), device.id)
        maps = [self.relMap()]
        databases = []
        for tname, instances in results.iteritems():
            if tname.startswith('si_'):
                for inst in instances:
                    om = self.objectMap(inst)
                    om.dbsiname = tname[3:]
                    om.id = self.prepId(om.dbsiname)
                    om.setProductKey = MultiArgs('MySQL Server %s (%s)'%(
                                        om.version, om.setProductKey), 'MySQL')
                    have = results.get('vr_%s'%om.dbsiname,[])
                    om.have = [h['have'][5:] for h in have]
                    maps[-1].append(om)
            elif tname.startswith('vr_'): continue 
            else: databases.extend(instances)
        self.relname = "softwaredatabases"
        self.modname = "ZenPacks.community.MySQLMon.MySqlDatabase"
        maps.append(self.relMap())
        for database in databases:
            try:
                om = self.objectMap(database)
                om.id = self.prepId('%s_%s'%(om.setDBSrvInst, om.dbname))
                om.activeTime = str(om.activeTime)
                om.setDBSrvInst = str(om.setDBSrvInst)
            except AttributeError:
                continue
            maps[-1].append(om)
        return maps
