FROM postgres:16

#COPY ./init.sh /docker-entrypoint-initdb.d/init.sh
COPY ./db_dump.sql /docker-entrypoint-initdb.d/db_dump.sql
CMD ["docker-entrypoint.sh", "postgres"]
