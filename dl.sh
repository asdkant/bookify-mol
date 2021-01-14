#!/bin/bash 
mkdir -p dl/arc{1,2,3}

for i in {1..9}; do
	wget -bq https://www.fictionpress.com/s/2961893/$i/Mother-of-Learning -O dl/arc1/00$i.html 
	echo $i ; sleep 0.5
done

for i in {10..26}; do
	wget -bq https://www.fictionpress.com/s/2961893/$i/Mother-of-Learning -O dl/arc1/0$i.html 
	echo $i ; sleep 0.5
done

for i in {27..54}; do
	wget -bq https://www.fictionpress.com/s/2961893/$i/Mother-of-Learning -O dl/arc2/0$i.html 
	echo $i ; sleep 0.5
done

for i in {55..99}; do
	wget -bq https://www.fictionpress.com/s/2961893/$i/Mother-of-Learning -O dl/arc3/0$i.html 
	echo $i ; sleep 0.5
done

for i in {100..108}; do
	wget -bq https://www.fictionpress.com/s/2961893/$i/Mother-of-Learning -O dl/arc3/$i.html 
	echo $i ; sleep 0.5
done


echo "Done!"
