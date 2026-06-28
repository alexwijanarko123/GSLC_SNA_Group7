# Stage 1: Building with Node.js (Vite)
FROM node:22-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build 

# Stage 2: Serving with Nginx
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Copy Vite build result from destination folder to Nginx directory
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/log/nginx && chmod 777 /var/log/nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]