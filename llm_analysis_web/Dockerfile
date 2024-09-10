# Use Node.js as the base image for building the app
FROM node:18 as build-stage

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app's source code
COPY . .

# Build the app
RUN npm run build

# Use an Nginx server as the production server
FROM nginx:stable-alpine as production-stage

# Copy the built app from the build stage to the Nginx html directory
COPY --from=build-stage /app/dist/spa /usr/share/nginx/html

# Copy custom Nginx configuration (optional)
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose the default Nginx HTTP port
EXPOSE 80

# Start the Nginx server
CMD ["nginx", "-g", "daemon off;"]
