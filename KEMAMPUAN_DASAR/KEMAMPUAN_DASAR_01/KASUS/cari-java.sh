#!/bin/bash
if [[ $(find $1 -name "*.java") ]]; then
echo "Ada file Java pada direktori"
find $1 -iname "*.java"
else
echo "Tidak ada file java"
fi

$ cari-java.sh $HOME/src
Ada file Java pada direktori /home/bpdp/src/hari-01

ike@adel:~$ sudo find / -iname *java
/usr/lib/jvm/java-11-openjdk-amd64/bin/java
/usr/lib/jvm/default-java
/usr/lib/libreoffice/share/Scripts/java
/usr/lib/libreoffice/share/Scripts/java/Highlight/HighlightText.java
/usr/lib/libreoffice/share/Scripts/java/HelloWorld/HelloWorld.java
/usr/lib/libreoffice/share/Scripts/java/MemoryUsage/MemoryUsage.java
/usr/share/bash-completion/completions/java
/usr/share/bison/skeletons/lalr1.java
/usr/share/java
/usr/share/code/resources/app/extensions/java
/usr/share/ca-certificates-java
/usr/share/bug/libjuh-java
/usr/share/bug/libridl-java
/usr/share/bug/libjurt-java
/usr/share/bug/libunoil-java
/usr/share/bug/libunoloader-java
/usr/share/doc/libjsp-api-java
/usr/share/doc/libservlet-api-java
/usr/share/doc/libjuh-java
/usr/share/doc/libridl-java
/usr/share/doc/bison/examples/java
/usr/share/doc/libhsqldb1.8.0-java
/usr/share/doc/libjurt-java
/usr/share/doc/libwebsocket-api-java
/usr/share/doc/libel-api-java
/usr/share/doc/libunoil-java
/usr/share/doc/ca-certificates-java
/usr/share/doc/libservlet3.1-java
/usr/share/doc/libunoloader-java
/usr/share/lintian/data/java
/usr/share/lintian/checks/languages/java
/usr/share/lintian/overrides/libjuh-java
/usr/share/lintian/overrides/libjurt-java
/usr/bin/java
/var/lib/dpkg/alternatives/java
find: ‘/run/user/1000/gvfs’: Permission denied
/etc/alternatives/java
/etc/.java
/etc/ssl/certs/java
/etc/apparmor.d/abstractions/ubuntu-browsers.d/java

