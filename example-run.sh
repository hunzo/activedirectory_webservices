docker run -d \
	--name web-services \
	-p 8088:5000 \
	-e DOMAIN_NAME="domain.local" \
	-e BASE_DN="dc=domain,dc=local" \
	-e BIND_USER="binduser" \
	-e BIND_PASSWORD="password" \
	-e AD_SERVER="192.168.1.100" \
	-e TOKEN_KEY="key_token" \
	img/images_name

