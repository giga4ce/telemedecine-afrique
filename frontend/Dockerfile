# Multi-stage: production Vite build served by nginx on port 80.
# Versions pinned for reproducible local<->OVH builds.
FROM node:22-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1.27-alpine
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

# Basic HTTP healthcheck on the root (busybox wget ships with nginx:alpine).
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=5 \
    CMD wget -q --spider http://localhost:80/ || exit 1
