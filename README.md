# CLUSTERING with Python Backend and Vue.js Frontend

## marcusgsta-ai.info - to see app in production

### Set up Python Virtural Environment (tester in terminal on MacOs)

```
python3.6 -m venv venv36
source venv36/bin/activate

pip install flask flask_restful flask_cors
```

### Start backend Python server
```
cd backend/
FLASK_APP=server.py FLASK_DEBUG=1 flask run
```
### or start like this
```
cd backend/
python3 server.py

```

# Set up Vue.js Frontend with vue-cli

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
