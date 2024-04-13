# Once:
#     docker pull mysql
#
# Enter 
#     mysql sandbox --password=password


docker run \
    --name mysql-sandbox \
    -e MYSQL_ROOT_PASSWORD=password \
    -e MYSQL_DATABASE=sandbox \
    -v ./init.d:/docker-entrypoint-initdb.d \
    -p 3306:3306 \
    -it -d mysql:latest 
