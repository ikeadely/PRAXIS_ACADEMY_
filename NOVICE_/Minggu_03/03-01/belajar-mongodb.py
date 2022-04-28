ike@adel:~$ sudo service mongodb start
[sudo] password for ike:            
ike@adel:~$ sudo service mongodb status
● mongodb.service - An object/document-oriented database
     Loaded: loaded (/lib/systemd/system/mongodb.service; enabled; vendo>
     Active: active (running) since Wed 2022-04-27 09:06:36 WIB; 2h 14mi>
       Docs: man:mongod(1)
   Main PID: 723 (mongod)
      Tasks: 23 (limit: 2108)
     Memory: 9.2M
     CGroup: /system.slice/mongodb.service
ike@adel:~$ sudo service mongodb stop
ike@adel:~$ mkdir -p cobamongo/db
ike@adel:~$ mongod --dbpath cobamongo/db/
2022-04-27T11:23:43.706+0700 I CONTROL  [initandlisten] MongoDB starting : pid=9645 port=27017 dbpath=cobamongo/db/ 64-bit host=adel
2022-04-27T11:23:43.716+0700 I CONTROL  [initandlisten] db version v3.6.8
2022-04-27T11:23:43.716+0700 I CONTROL  [initandlisten] git version: 8e540c0b6db93ce994cc548f000900bdc740f80a
2022-04-27T11:23:43.716+0700 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.1.1f  31 Mar 2020
2022-04-27T11:23:43.716+0700 I CONTROL  [initandlisten] allocator: tcmalloc
2022-04-27T11:23:43.716+0700 I CONTROL  [initandlisten] modules: none
2022-04-27T11:23:43.716+0700 I CONTROL  [initandlisten] build environment:
2022-04-27T11:23:43.716+0700 I CONTROL  [initandlisten]     distarch: x86_64
2022-04-27T11:23:43.716+0700 I CONTROL  [initandlisten]     target_arch: x86_64
2022-04-27T11:23:43.716+0700 I CONTROL  [initandlisten] options: { storage: { dbPath: "cobamongo/db/" } }
2022-04-27T11:23:43.726+0700 I STORAGE  [initandlisten] 
2022-04-27T11:23:43.726+0700 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2022-04-27T11:23:43.726+0700 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2022-04-27T11:23:43.752+0700 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=412M,session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),cache_cursors=false,compatibility=(release="3.0",require_max="3.0"),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),
2022-04-27T11:23:45.403+0700 I STORAGE  [initandlisten] WiredTiger message [1651033425:403271][9645:0x7efdf14e2ac0], txn-recover: Set global recovery timestamp: 0
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] 
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] 
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] ** WARNING: This server is bound to localhost.
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] **          Remote systems will be unable to connect to this server. 
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] **          Start the server with --bind_ip <address> to specify which IP 
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] **          addresses it should serve responses from, or with --bind_ip_all to
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] **          bind to all interfaces. If this behavior is desired, start the
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] **          server with --bind_ip 127.0.0.1 to disable this warning.
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] 
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] 
2022-04-27T11:23:46.919+0700 I CONTROL  [initandlisten] ** WARNING: soft rlimits too low. rlimits set to 7027 processes, 1048576 files. Number of processes should be at least 524288 : 0.5 times number of files.
2022-04-27T11:23:47.841+0700 I STORAGE  [initandlisten] createCollection: admin.system.version with provided UUID: 67922a40-f86a-4298-9a9c-92c9213aa229
2022-04-27T11:23:48.314+0700 I COMMAND  [initandlisten] setting featureCompatibilityVersion to 3.6
2022-04-27T11:23:48.352+0700 I STORAGE  [initandlisten] createCollection: local.startup_log with generated UUID: 0220f002-8011-43c7-abf5-070f3744aad4
2022-04-27T11:23:48.650+0700 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory 'cobamongo/db/diagnostic.data'
2022-04-27T11:23:48.650+0700 I NETWORK  [initandlisten] waiting for connections on port 27017
2022-04-27T11:23:48.651+0700 I STORAGE  [LogicalSessionCacheRefresh] createCollection: config.system.sessions with generated UUID: 4ed65b38-9915-455e-b555-2f79f1bb5db4
2022-04-27T11:23:49.466+0700 I INDEX    [LogicalSessionCacheRefresh] build index on: config.system.sessions properties: { v: 2, key: { lastUse: 1 }, name: "lsidTTLIndex", ns: "config.system.sessions", expireAfterSeconds: 1800 }
2022-04-27T11:23:49.466+0700 I INDEX    [LogicalSessionCacheRefresh]     building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2022-04-27T11:23:49.516+0700 I INDEX    [LogicalSessionCacheRefresh] build index done.  scanned 0 total records. 0 secs
2022-04-27T11:23:49.516+0700 I COMMAND  [LogicalSessionCacheRefresh] command config.$cmd command: createIndexes { createIndexes: "system.sessions", indexes: [ { key: { lastUse: 1 }, name: "lsidTTLIndex", expireAfterSeconds: 1800 } ], $db: "config" } numYields:0 reslen:98 locks:{ Global: { acquireCount: { r: 2, w: 2 } }, Database: { acquireCount: { w: 2, W: 1 } }, Collection: { acquireCount: { w: 2 } } } protocol:op_msg 865ms
sudo service mongodb start
^C2022-04-27T11:25:11.181+0700 I CONTROL  [signalProcessingThread] got signal 2 (Interrupt), will terminate after current cmd ends
2022-04-27T11:25:11.181+0700 I NETWORK  [signalProcessingThread] shutdown: going to close listening sockets...
2022-04-27T11:25:11.181+0700 I NETWORK  [signalProcessingThread] removing socket file: /tmp/mongodb-27017.sock
2022-04-27T11:25:11.183+0700 I FTDC     [signalProcessingThread] Shutting down full-time diagnostic data capture
2022-04-27T11:25:11.188+0700 I STORAGE  [signalProcessingThread] WiredTigerKVEngine shutting down
2022-04-27T11:25:11.715+0700 I STORAGE  [signalProcessingThread] shutdown: removing fs lock...
2022-04-27T11:25:11.715+0700 I CONTROL  [signalProcessingThread] now exiting
2022-04-27T11:25:11.715+0700 I CONTROL  [signalProcessingThread] shutting down with code:0
ike@adel:~$ sudo service mongodb start
ike@adel:~$ mongo
MongoDB shell version v3.6.8
connecting to: mongodb://127.0.0.1:27017
Implicit session: session { "id" : UUID("09d9ea7a-f313-473a-bcd0-0ab5c922da35") }
MongoDB server version: 3.6.8
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
        http://docs.mongodb.org/
Questions? Try the support group
        http://groups.google.com/group/mongodb-user
Server has startup warnings: 
2022-04-27T11:25:26.743+0700 I STORAGE  [initandlisten] 
2022-04-27T11:25:26.743+0700 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2022-04-27T11:25:26.743+0700 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2022-04-27T11:25:29.534+0700 I CONTROL  [initandlisten] 
2022-04-27T11:25:29.534+0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2022-04-27T11:25:29.534+0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2022-04-27T11:25:29.534+0700 I CONTROL  [initandlisten] 
> db
test
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> ^C
bye
ike@adel:~$ mongo
MongoDB shell version v3.6.8
connecting to: mongodb://127.0.0.1:27017
Implicit session: session { "id" : UUID("6ec2e7f3-ba09-4ae5-8f03-68c410922252") }
MongoDB server version: 3.6.8
Server has startup warnings: 
2022-04-27T11:25:26.743+0700 I STORAGE  [initandlisten] 
2022-04-27T11:25:26.743+0700 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2022-04-27T11:25:26.743+0700 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2022-04-27T11:25:29.534+0700 I CONTROL  [initandlisten] 
2022-04-27T11:25:29.534+0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2022-04-27T11:25:29.534+0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2022-04-27T11:25:29.534+0700 I CONTROL  [initandlisten] 
> db
test
> use tokobuku
switched to db tokobuku
> db tokobuku
2022-04-27T11:28:25.468+0700 E QUERY    [thread1] SyntaxError: missing ; before statement @(shell):1:3
> db.createCollections("nama_koleksi")
2022-04-27T11:29:02.289+0700 E QUERY    [thread1] TypeError: db.createCollections is not a function :
@(shell):1:1
> db.<koleksi>.insert(<data>)
2022-04-27T11:29:43.372+0700 E QUERY    [thread1] SyntaxError: missing name after . operator @(shell):1:3
> db.buku.insert({
...     judul: "Belajar MongoDB",
...     sinopsis: "Panduan MongoDB untuk Pemula",
...     pengarang: "Petani Kode"
... })
WriteResult({ "nInserted" : 1 })
> db.buku.insert({
...     judul: "Pemrograman Javascript dan MongoDB",
...     sinopsis: "Panduan Pemrograman Js dan MongoDB",
...     pengarang: "Petani Kode",
...     harga: 98000
... })
WriteResult({ "nInserted" : 1 })
> db.buku.count()
2
> db.buku.find()
{ "_id" : ObjectId("6268c6eb08372d48c01460e4"), "judul" : "Belajar MongoDB", "sinopsis" : "Panduan MongoDB untuk Pemula", "pengarang" : "Petani Kode" }
{ "_id" : ObjectId("6268c70208372d48c01460e5"), "judul" : "Pemrograman Javascript dan MongoDB", "sinopsis" : "Panduan Pemrograman Js dan MongoDB", "pengarang" : "Petani Kode", "harga" : 98000 }
> db.buku.find().pretty()
{
        "_id" : ObjectId("6268c6eb08372d48c01460e4"),
        "judul" : "Belajar MongoDB",
        "sinopsis" : "Panduan MongoDB untuk Pemula",
        "pengarang" : "Petani Kode"
}
{
        "_id" : ObjectId("6268c70208372d48c01460e5"),
        "judul" : "Pemrograman Javascript dan MongoDB",
        "sinopsis" : "Panduan Pemrograman Js dan MongoDB",
        "pengarang" : "Petani Kode",
        "harga" : 98000
}
> db.buku.fing({ harga: 98000 })
2022-04-27T11:50:26.724+0700 E QUERY    [thread1] TypeError: db.buku.fing is not a function :
@(shell):1:1
> db.buku.find({ harga: 98000 })
{ "_id" : ObjectId("6268c70208372d48c01460e5"), "judul" : "Pemrograman Javascript dan MongoDB", "sinopsis" : "Panduan Pemrograman Js dan MongoDB", "pengarang" : "Petani Kode", "harga" : 98000 }
> 



dilakukan pada terminal
cek 


