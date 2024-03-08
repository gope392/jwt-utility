# Jwt-utility:
Basic JWT utility that allows to generate and validate tokens implemented in Python 3.

### Configuration:
Running this utility requires a few parameters configuration.

### Input Data:
- Custom data included on the JWT Payload.
- Should be specified on `docker-compose.yml` file as env_variable: `INPUT_DATA`

### Secret:
- Hex String to sign the JWT using the 'HS512' algorithm
- Independent `secret.txt` file specificed within `docker-compose.yml` and located on app folder `/jwt-utility`.

### Running with Makefile:
- Included Makefile allow to Build and Run the Utility using Docker-Compose.

### Build utility Docker Image:
- Using Python 3.10 and Alpine as Base Image

```
make build
```

### Run utility:

```
make run
```

### Stop utility:
- This also delete all containers

```
make stop
```





