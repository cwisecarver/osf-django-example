#!/usr/bin/env bash
set -e

while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -r|--reset)
    RESET_DB="yessir"
    ;;
    *)
    # unknown option
    ;;
esac
shift
done

pip install -U -r requirements/local-dev.txt

if [ -n "$RESET_DB" ]; then
    python manage.py reset_db --noinput
fi

python manage.py migrate
python manage.py runserver_plus 127.0.0.1:8010


