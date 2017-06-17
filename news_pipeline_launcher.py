#!/usr/bin/env bash
radis-server
mongod

pip install -r requirements.txt

cd news_pipeline
python news_monitor.py &
python news_fetcher.py &
python news_deduper.py &

echo "===~~~ launcher======="
read -p "PRESS [ENTER] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)
