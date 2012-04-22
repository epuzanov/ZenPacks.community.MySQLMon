================================
ZenPacks.community.MySQLMon
================================

About
=====

This project is `Zenoss <http://www.zenoss.com/>`_ extension (ZenPack) that
makes it possible to model and monitor MySQL databases.
databases.

Requirements
============

Zenoss
------

You must first have, or install, Zenoss 2.5.2 or later. This ZenPack was tested
against Zenoss 2.5.2 and Zenoss 3.2. You can download the free Core version of
Zenoss from http://community.zenoss.org/community/download

ZenPacks
--------

You must first install

- `SQLDataSource ZenPack <http://community.zenoss.org/docs/DOC-5913>`_
- `RDBMS Monitoring ZenPack <http://community.zenoss.org/docs/DOC-3447>`_

If you have an old version (ZenPacks.community.MySQLMon_ODBC) of this ZenPack
installed, please uninstall it first.

External dependencies
---------------------

You can use **pyisqldb** module provided by SQLDataSource ZenPack in combination
with MySQL ODBC driver, or install Python DB-API 2.0 compatible **MySQLdb**
module.

- **pyisqldb** - DB-API 2.0 compatible wrapper for **isql** command from
  `unixODBC <http://www.unixodbc.org/>`_. MySQL ODBC driver must be
  installed and registered with name "MySQL".

  zMySqlConnectionString example:

      ::

          'pyisqldb','DRIVER={MySQL};SERVER=${here/manageIp};PORT=${here/port};DATABASE=information_schema;UID=${here/zMySQLUsername};PWD=${here/zMySQLPassword}'

- `pyodbc <http://code.google.com/p/pyodbc/>`_ - DB-API 2.0 compatible interface
  to unixODBC. MySQL ODBC driver must be installed and registered with name
  "MySQL".

  zMySqlConnectionString example:

      ::

          'pyodbc','DRIVER={MySQL};SERVER=${here/manageIp};PORT=${here/port};DATABASE=information_schema;UID=${here/zMySQLUsername};PWD=${here/zMySQLPassword}'

- **MySQLdb** - DB-API 2.0 compatible Pure-Python interface to the MySQL database.

  zMySqlConnectionString example:

      ::

          'MySQLdb',host='${here/manageIp}',port=${here/port},db='information_schema',user='${here/zMySqlUsername}',passwd='${here/zMySqlPassword}'

Installation
============

Normal Installation (packaged egg)
----------------------------------

Download the `MySQLMon ZenPack <http://community.zenoss.org/docs/DOC-3388>`_.
Copy this file to your Zenoss server and run the following commands as the zenoss
user.

    ::

        zenpack --install ZenPacks.community.MySQLMon-3.2.egg
        zenoss restart

Developer Installation (link mode)
----------------------------------

If you wish to further develop and possibly contribute back to the MySQLMon
ZenPack you should clone the git `repository <https://github.com/epuzanov/ZenPacks.community.MySQLMon>`_,
then install the ZenPack in developer mode using the following commands.

    ::

        git clone git://github.com/epuzanov/ZenPacks.community.MySQLMon.git
        zenpack --link --install ZenPacks.community.MySQLMon
        zenoss restart


Usage
=====

Installing the ZenPack will add the following items to your Zenoss system.

Configuration Properties
------------------------

- zMySqlConnectionString - connection string template.
- zMySqlPorts - list of TCP ports
- zMySqlUsername - username
- zMySqlPassword - password

Modeler Plugins
---------------

- community.sql.MySqlDatabaseMap

Monitoring Templates
--------------------

- MySqlSrvInst
- MySqlTablespace

Performance graphs
------------------

Database Server Instance

- MySQL - Command Statistics
- MySQL - Select Statistics
- MySQL - Handler Statistics
- MySQL - Network Traffic

Database

- MySQL - Database Size
 