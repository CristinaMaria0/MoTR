# syntax=docker/dockerfile:1

ARG NODE_VERSION=16.20.2
FROM node:${NODE_VERSION}

WORKDIR /usr/src/app

# Copy package.json from the correct location
COPY MoTR/run_motr_in_magpie/attachment/package*.json ./

# ✅ Install Vue CLI globally
RUN npm install -g @vue/cli

# ✅ Install project dependencies
RUN npm install

# Copy the rest of the project
COPY MoTR/run_motr_in_magpie/attachment ./


# ✅ Build the Vue.js app using Vue CLI
# RUN npm run serve
RUN npm run build

# Ensure `dist/` is not empty
RUN ls -l dist/
# ✅ Install a static file server
RUN npm install -g serve

# Set a non-root user AFTER installation
USER node

# Expose the application port
EXPOSE 3000

# ✅ Serve the built Vue app using a static server
CMD ["npx", "serve", "-s", "dist", "-l", "3000"]
