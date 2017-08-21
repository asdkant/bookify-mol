#!/bin/bash 

lastarc=$(ls dl/arc? -d -1 | tr -d 'dl/arc' | tail -1)
lastchap=$(ls $(ls dl/arc? -d -1 | tail -1) | tail -1 | tr -d '.html')
outfile='Mother of Learning a1c01-a'$lastarc'c'$lastchap' - nobody103 (Domagoj Kurmaic).html'


for a in $(ls dl/arc? -d -1 | tr -d 'dl/arc') ; do # a == 1, 2, 3, etc.
	echo '<h1>Arc '$a'</h1>' >> "$outfile"
	echo "=== Arc $a ==="
	for c in dl/arc${a}/*.html; do
		./chapextract.py $c >> "$outfile"
		echo "chapter $c" | sed -e 's|dl/arc./||g' | sed -e 's/\.html//g'
	done
done