#!/bin/sh
port=8080
ts=`date "+%s"`
params="--db_filename=skip --result_db_filename=skip --log_file=proddump.log" 
echo "$1" | python "`cygpath -w "/cygdrive/c/Program Files/Google/google_appengine//bulkloader.py"`" --dump --filename=proddump.$ts.dump --kind=Gaest --url=http://vristbryllup.appspot.com/remote_api --email=svrist@gmail.com --passin $params
echo "" | python "`cygpath -w "/cygdrive/c/Program Files/Google/google_appengine//bulkloader.py"`" --restore --filename=proddump.$ts.dump --kind=Gaest --url=http://localhost:$port/remote_api --email=test@example.org --passin --app_id=vristbryllup $params
