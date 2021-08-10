FROM node:14.6.0

RUN mkdir -p /client
WORKDIR /client
COPY /client/package*.json /client/
RUN npm install
COPY client  /client
CMD ["npm", "run", "start"]
