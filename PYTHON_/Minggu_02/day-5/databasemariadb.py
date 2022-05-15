sudo mysql
[sudo] password for ike:            
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 43
Server version: 10.3.34-MariaDB-0ubuntu0.20.04.1 Ubuntu 20.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| performance_schema |
+--------------------+
2 rows in set (0.001 sec)

MariaDB [(none)]> create database latihan;
Query OK, 1 row affected (0.034 sec)

MariaDB [(none)]> use latihan;
Database changed
MariaDB [latihan]> create table tabel_biodata (nama char(20), alamat char(50), telp char(15));
Query OK, 0 rows affected (0.145 sec)

MariaDB [latihan]> desc tabel_biodata;
+--------+----------+------+-----+---------+-------+
| Field  | Type     | Null | Key | Default | Extra |
+--------+----------+------+-----+---------+-------+
| nama   | char(20) | YES  |     | NULL    |       |
| alamat | char(50) | YES  |     | NULL    |       |
| telp   | char(15) | YES  |     | NULL    |       |
+--------+----------+------+-----+---------+-------+
3 rows in set (0.002 sec)

MariaDB [latihan]> insert into tabel_bidata values('adel', 'Trangkil', '085601994257'
    -> select * from tabel_biodata;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'select * from tabel_biodata' at line 2
MariaDB [latihan]> select nama, alamat, telp from tabel_biodata;
Empty set (0.046 sec)

MariaDB [latihan]> desc tabel_biodata;
+--------+----------+------+-----+---------+-------+
| Field  | Type     | Null | Key | Default | Extra |
+--------+----------+------+-----+---------+-------+
| nama   | char(20) | YES  |     | NULL    |       |
| alamat | char(50) | YES  |     | NULL    |       |
| telp   | char(15) | YES  |     | NULL    |       |
+--------+----------+------+-----+---------+-------+
3 rows in set (0.003 sec)

MariaDB [latihan]> insert into tabel_bidata values('Adel','Trangkil','085601994257'
    -> select nama, alamat, telp from tabel_biodata;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'select nama, alamat, telp from tabel_biodata' at line 2
MariaDB [latihan]> insert into tabel_biodata values('Adel','Trangkil','085601994257'
    -> select nama, alamat, telp from tabel_biodata;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'select nama, alamat, telp from tabel_biodata' at line 2
MariaDB [latihan]> insert into tabel_biodata values('Adel','Trangkil','085601994257');
Query OK, 1 row affected (0.092 sec)

MariaDB [latihan]> select * from tabel_biodata;
+------+----------+--------------+
| nama | alamat   | telp         |
+------+----------+--------------+
| Adel | Trangkil | 085601994257 |
+------+----------+--------------+
1 row in set (0.001 sec)

MariaDB [latihan]>  Ctrl-C -- exit!
Aborted


menggunakan mysql setelah ??.txt dijalankan

$ sudo mysql
[sudo] password for ike:            
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.29-0ubuntu0.20.04.3 (Ubuntu)

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show database;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'database' at line 1
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0,63 sec)

mysql> create database adel
    -> create database adel;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'create database adel' at line 2
mysql> \c
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0,00 sec)

mysql> create database latihan;
Query OK, 1 row affected (0,25 sec)

mysql> use latihan;
Database changed
mysql> create table tabel_nama (nama char(20), tempat char(70));
Query OK, 0 rows affected (0,97 sec)

mysql> desc tabel_nama;
+--------+----------+------+-----+---------+-------+
| Field  | Type     | Null | Key | Default | Extra |
+--------+----------+------+-----+---------+-------+
| nama   | char(20) | YES  |     | NULL    |       |
| tempat | char(70) | YES  |     | NULL    |       |
+--------+----------+------+-----+---------+-------+
2 rows in set (0,09 sec)

mysql> exit
Bye


~$ sudo mariadb
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 10
Server version: 10.3.34-MariaDB-0ubuntu0.20.04.1 Ubuntu 20.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| praxis             |
+--------------------+
4 rows in set (0.001 sec)

MariaDB [(none)]> DROP DATABASES praxis;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'DATABASES praxis' at line 1
MariaDB [(none)]> DROP DATABASE praxis;
Query OK, 0 rows affected (0.188 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.000 sec)

MariaDB [(none)]> 

ike@adel:~$ sudo mariadb
[sudo] password for ike:            
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 8
Server version: 10.3.34-MariaDB-0ubuntu0.20.04.1 Ubuntu 20.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| film               |
| information_schema |
| mysql              |
| pelatihan          |
| performance_schema |
+--------------------+
5 rows in set (0.378 sec)

MariaDB [(none)]> use pelatihan
Database changed
MariaDB [pelatihan]> create table tabel_pelatihan (nama char(20), umur char(50));
Query OK, 0 rows affected (1.446 sec)

MariaDB [pelatihan]> desv tabel_pelatihan;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'desv tabel_pelatihan' at line 1
MariaDB [pelatihan]> desc tabel_pelatihan;
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| nama  | char(20) | YES  |     | NULL    |       |
| umur  | char(50) | YES  |     | NULL    |       |
+-------+----------+------+-----+---------+-------+
2 rows in set (0.128 sec)

MariaDB [pelatihan]> insert into tabel_pelatihan values('chamidcha', '29');
ERROR 2006 (HY000): MySQL server has gone away
No connection. Trying to reconnect...
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
ERROR: Can't connect to the server

unknown [pelatihan]> 
