# Use an official NGINX base image
FROM nginx:stable-alpine

# Set maintainer metadata (opzionale)
LABEL maintainer="tuo.nome@example.com"

# Copy static website files into the default NGINX html folder
# (assicurati di avere una cartella “html/” con i file web)
#COPY ./html /usr/share/nginx/html

# Copy custom NGINX configuration if presente
# (opzionale, puoi commentare se non serve)
# COPY ./nginx.conf /etc/nginx/nginx.conf

# Espone la porta HTTP standard
EXPOSE 80

# Start NGINX in the foreground (entrypoint di default)
CMD ["nginx", "-g", "daemon off;"]
