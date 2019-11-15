# Introduction 
Active Directory Management Web Services
# Build and Test
Build Docker Images and Run Container with Parameter
## Build docker images
	- docker build -t img/images_name .
## Run container with parameter
```
docker run -d \
        --name active_directory_webservices \
        -p 8088:5000 \
        -e DOMAIN_NAME="domain.local" \
        -e BASE_DN="dc=domain,dc=local" \
        -e BIND_USER="binduser" \
        -e BIND_PASSWORD="bind_user_password" \
        -e AD_SERVER="192.168.1.10" \
        -e TOKEN_KEY="token_key" \
	img/images_name
```
## Environment Variable
```
DOMAIN_NAME : active directory domain name
BASE_DN : base dn for search account 
BIND_USER : bind username with privilege 'Account Operation'
BIND_PASSWORD : bind user password
AD_SERVER : active directory ip address
TOKEN_KEY : Token Keys
```
## Run Container with docker-compose
Edit docker-compose.yml set Environment Variable
```
docker-compose up -d --build
```
