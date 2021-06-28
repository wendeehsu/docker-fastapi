# DevOps Backend Example

## Info
- `python=3.9`
- `fastapi` framework, with `async`

## Test service locally
1. Prepare `python` environment, e.g. with `conda`
```shell
conda create --name be-example python=3.9
conda activate be-example
```

2. Install dependencies
```shell
pip install -r requirements.txt
pip install uvicorn
```

3. Start
```shell
uvicorn app:app
```

And you will see, in your terminal, that uvicorn is running at a specific location e.g. `http://localhost:8000`

### To test if it works

Go to `/docs` and you will see a interactable documentation UI of working functions.  
If the service is running at `http://localhost:8000`, the documentation UI will be at `http://localhost:8000/docs`.


### Configuration
Config with environment variables or `.env` file.
If `.env` is given, the settings in `.env` will override OS environment variables.

Example can be checked in `.env.example`.

Note: `DB_VENDOR` should fill in either `postgresql` or `mysql`.