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

