### Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r reqirements.txt
```

### Commands
db migration in docker
```bash
docker-compose exec flask python src/db-init.py
```

run tests in docker
```bash
docker-compose exec flask pytest src/tests
```
