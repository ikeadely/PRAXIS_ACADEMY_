Ringkasan: dalam tutorial ini, Anda akan belajar tentang tabel sementara PostgreSQL dan cara mengelolanya secara efektif.
Membuat tabel sementara PostgreSQL

Tabel sementara, seperti namanya tersirat, adalah tabel berumur pendek yang ada selama sesi database. PostgreSQL secara otomatis menjatuhkan tabel sementara di akhir sesi atau transaksi.

Untuk membuat tabel sementara, Anda menggunakan pernyataan CREATE TEMPORARY TABLE.
Dalam sintaks ini:

    Pertama, tentukan nama tabel sementara setelah kata kunci CREATE TEMPORARY TABLE.
    Kedua, tentukan daftar kolom, yang sama dengan yang ada di pernyataan CREATE TABLE.

Kata kunci TEMP dan SEMENTARA setara sehingga Anda dapat menggunakannya secara bergantian:

Tabel sementara hanya terlihat oleh sesi yang membuatnya. Dengan kata lain, itu tidak terlihat oleh sesi lain.

Mari kita lihat sebuah contoh.

Pertama, login ke server database PostgreSQL menggunakan program psql dan buat database baru bernama test:

Selanjutnya, buat tabel sementara bernama mytemp sebagai berikut:

Bahasa kode: dialek SQL PostgreSQL dan PL/pgSQL (pgsql)

Kemudian, luncurkan sesi lain yang terhubung ke database pengujian dan data kueri dari tabel mytemp:

Seperti yang dapat dilihat dengan jelas dari output, sesi kedua tidak dapat melihat tabel mytemp. Hanya sesi pertama yang dapat mengaksesnya.

Setelah itu, keluar dari semua sesi:

Terakhir, login ke server database lagi dan kueri data dari tabel mytemp:

Tabel mytemp tidak ada karena telah dijatuhkan secara otomatis ketika sesi berakhir, oleh karena itu, PostgreSQL mengeluarkan kesalahan.
Nama tabel sementara PostgreSQL

Tabel sementara dapat berbagi nama yang sama dengan tabel permanen, meskipun tidak disarankan.

Saat Anda membuat tabel sementara yang memiliki nama yang sama dengan tabel permanen, Anda tidak dapat mengakses tabel permanen hingga tabel sementara dihapus. Perhatikan contoh berikut:

Pertama, buat tabel bernama pelanggan:
Kedua, buat tabel sementara dengan nama yang sama: pelanggan
Sekarang, kueri data dari tabel pelanggan:

Kali ini PostgreSQL mengakses pelanggan tabel sementara, bukan pelanggan permanen.

Mulai sekarang, Anda hanya dapat mengakses tabel pelanggan permanen di sesi saat ini ketika pelanggan tabel sementara dihapus secara eksplisit.

Perhatikan bahwa PostgreSQL membuat tabel sementara dalam skema khusus, oleh karena itu, Anda tidak dapat menentukan skema dalam pernyataan CREATE TEMP TABLE.

Jika Anda mencantumkan tabel dalam database pengujian, Anda hanya akan melihat pelanggan tabel sementara, bukan pelanggan permanen:

Output menunjukkan skema tabel sementara pelanggan adalah pg_temp_3.
Menghapus tabel sementara PostgreSQL

Untuk menjatuhkan tabel sementara, Anda menggunakan pernyataan DROP TABLE. Pernyataan berikut mengilustrasikan cara menghapus tabel sementara:

Berbeda dengan pernyataan CREATE TABLE, pernyataan DROP TABLE tidak memiliki kata kunci TEMP atau SEMENTARA yang dibuat khusus untuk tabel sementara.

Misalnya, pernyataan berikut menghapus pelanggan tabel sementara yang telah kami buat dalam contoh di atas:

Jika Anda membuat daftar tabel di database pengujian lagi, pelanggan tabel permanen akan muncul sebagai berikut:

Dalam tutorial ini, Anda telah belajar tentang tabel sementara dan cara membuat dan melepaskannya menggunakan pernyataan CREATE TEMP TABLE dan DROP TABLE.

A Step-by-Step Guide To PostgreSQL Temporary Table
PostgreSQL Temporary Table

Summary: in this tutorial, you will learn about the PostgreSQL temporary table and how to manage it effectively.
Creating a PostgreSQL temporary table

A temporary table, as its named implied, is a short-lived table that exists for the duration of a database session. PostgreSQL automatically drops the temporary tables at the end of a session or a transaction.

To create a temporary table, you use the CREATE TEMPORARY TABLE statement.

CREATE TEMPORARY TABLE temp_table_name(
   column_list
);
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

In this syntax:

    First, specify the name of the temporary table after the CREATE TEMPORARY TABLE keywords.
    Second, specify the column list, which is the same as the one in the CREATE TABLE statement.

The TEMP and TEMPORARY keywords are equivalent so you can use them interchangeably:

CREATE TEMP TABLE temp_table(
   ...
);
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

A temporary table is visible only to the session that creates it. In other words, it is invisible to other sessions.

Let’s take a look at an example.

First, log in to the PostgreSQL database server using the psql program and create a new database named test:

postgres=# CREATE DATABASE test;
CREATE DATABASE
postgres-# \c test;
You are now connected to database "test" as user "postgres".
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

Next, create a temporary table named mytemp as follows:

test=# CREATE TEMP TABLE mytemp(c INT);
CREATE TABLE
test=# SELECT * FROM mytemp;
 c
---
(0 rows)
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

Then, launch another session that connects to the test database and query data from the mytemp table:

test=# SELECT * FROM mytemp;
ERROR:  relation "mytemp" does not exist
LINE 1: SELECT * FROM mytemp;
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

As can see clearly from the output, the second session could not see the mytemp table. Only the first session can access it.

After that, quit all the sessions:

test=# \q
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

Finally, login to the database server again and query data from the mytemp table:

test=# SELECT * FROM mytemp;
ERROR:  relation "mytemp" does not exist
LINE 1: SELECT * FROM mytemp;
                      ^
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

The mytemp table does not exist because it has been dropped automatically when the session ended, therefore, PostgreSQL issued an error.
PostgreSQL temporary table name

A temporary table can share the same name with a permanent table, even though it is not recommended.

When you create a temporary table that shares the same name with a permanent table, you cannot access the permanent table until the temporary table is removed. Consider the following example:

First, create a table named customers:

CREATE TABLE customers(
   id SERIAL PRIMARY KEY, 
   name VARCHAR NOT NULL
);
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

Second, create a temporary table with the same name: customers

CREATE TEMP TABLE customers(
    customer_id INT
);
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

Now, query data from the  customers table:

SELECT * FROM customers;
 customer_id
-------------
(0 rows)
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

This time PostgreSQL accessed the temporary table customers instead of the permanent one.

From now on, you can only access the permanent customers table in the current session when the temporary table customers is removed explicitly.

Note that PostgreSQL creates temporary tables in a special schema, therefore, you cannot specify the schema in the CREATE TEMP TABLE statement.

If you list the tables in the test database, you will only see the temporary table customers, not the permanent one:

                 List of relations
  Schema   |       Name       |   Type   |  Owner
-----------+------------------+----------+----------
 pg_temp_3 | customers        | table    | postgres
 public    | customers_id_seq | sequence | postgres
(2 rows)
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

The output shows the schema of the customers temporary table is pg_temp_3.
Removing a PostgreSQL temporary table

To drop a temporary table, you use the DROP TABLE statement. The following statement illustrates how to drop a temporary table:

DROP TABLE temp_table_name;
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

Unlike the CREATE TABLE statement, the DROP TABLE statement does not have the TEMP or TEMPORARY keyword created specifically for temporary tables.

For example, the following statement drops the temporary table customers that we have created in the above example:

DROP TABLE customers;
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

If you list the tables in the test database again, the permanent table customers will appear as follows:

test=# \d
                List of relations
 Schema |       Name       |   Type   |  Owner
--------+------------------+----------+----------
 public | customers        | table    | postgres
 public | customers_id_seq | sequence | postgres
(2 rows)
Code language: PostgreSQL SQL dialect and PL/pgSQL (pgsql)

In this tutorial, you have learned about the temporary table and how to create and drop it using CREATE TEMP TABLE and DROP TABLE statements.

