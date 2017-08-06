#!/bin/bash 
mkdir -p dl/arc{1,2,3}
curl 'https://www.fictionpress.com/s/2961893/[1-26]/Mother-of-Learning'  -o 'dl/arc1/#1.html'
curl 'https://www.fictionpress.com/s/2961893/[27-54]/Mother-of-Learning' -o 'dl/arc2/#1.html'
curl 'https://www.fictionpress.com/s/2961893/[55-72]/Mother-of-Learning' -o 'dl/arc3/#1.html'

