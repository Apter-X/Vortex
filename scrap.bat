#!/bin/sh

#$1 = Web site to screp
#$2 = Page start
#$3 = Page end
#$3 = Nombre de page par thread

echo "Site : $1"
echo "Start from : $2 to $3"

site=$1
from=$2
to=$3
nbpagethreed=$4

nb_pages=$(expr $to - $from)

echo "NB page to scrap : $nb_pages"

for ((i = $from; i <= $to; i = i + $nbpagethreed)); do
  page_start=$i
  page_end=$(expr \( $page_start + $nbpagethreed \))
  echo "$page_start TO $page_end"
  python3 ./app/main.py $site $page_start $page_end &
  sleep $((1 + $RANDOM % 3))
done
