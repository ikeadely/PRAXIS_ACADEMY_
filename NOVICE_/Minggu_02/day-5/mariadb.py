ike@adel:~$ pip3 install mariadb
Collecting mariadb
  Downloading mariadb-1.0.11.zip (85 kB)
     |████████████████████████████████| 85 kB 126 kB/s 
    ERROR: Command errored out with exit status 1:
     command: /usr/bin/python3 -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-rcbf6nlg/mariadb/setup.py'"'"'; __file__='"'"'/tmp/pip-install-rcbf6nlg/mariadb/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /tmp/pip-install-rcbf6nlg/mariadb/pip-egg-info
         cwd: /tmp/pip-install-rcbf6nlg/mariadb/
    Complete output (17 lines):
    /bin/sh: 1: mariadb_config: not found
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-install-rcbf6nlg/mariadb/setup.py", line 26, in <module>
        cfg = get_config(options)
      File "/tmp/pip-install-rcbf6nlg/mariadb/mariadb_posix.py", line 59, in get_config
        cc_version = mariadb_config(config_prg, "cc_version")
      File "/tmp/pip-install-rcbf6nlg/mariadb/mariadb_posix.py", line 28, in mariadb_config
        raise EnvironmentError(
    OSError: mariadb_config not found.
    
    Please make sure, that MariaDB Connector/C is installed on your system.
    Either set the environment variable MARIADB_CONFIG or edit the configuration
    file 'site.cfg' and set the 'mariadb_config option, which should point
    to the mariadb_config utility.
    The MariaDB Download website at <https://downloads.mariadb.com/Connectors/c/>
    provides latest stable releease of Connector/C.
    ----------------------------------------
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.

import mariadb
import sys

try:
    conn = mariadb.connect(
        user="db_user",
        password="db_user_passwd",
        host="192.0.2.1",
        port=3306,
        database="employees"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
    