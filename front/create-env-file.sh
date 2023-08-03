touch .env.production

for envvar in "$@" 
do
   echo "$envvar" >> .env.production
done
