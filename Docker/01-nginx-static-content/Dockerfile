# Use the Nginx base image on Alpine
FROM nginx:alpine

# Copy the static content to the Nginx directory
COPY content /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start the Nginx server
CMD ["nginx", "-g", "daemon off;"]
