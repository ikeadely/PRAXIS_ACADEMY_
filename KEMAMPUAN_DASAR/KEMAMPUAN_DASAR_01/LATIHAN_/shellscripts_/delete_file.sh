#!/bin/bash
echo "Enter filename to remove"
read fn
rm -i $fn

ike@adel:~$ nano delete_file.sh
ike@adel:~$ ls
delete_file.sh  Downloads  Pictures        README.md  Videos
Desktop         examples   PRAXIS-ACADEMY  Templates
Documents       Music      Public          TOKEN.txt
ike@adel:~$ bash delete_file.sh
Enter filename to remove
README.md
rm: remove regular file 'README.md'? y
ike@adel:~$ ls
delete_file.sh  Documents  examples  Pictures        Public     TOKEN.txt
Desktop         Downloads  Music     PRAXIS-ACADEMY  Templates  Videos

