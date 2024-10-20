#!/bin/bash
set -eo pipefail

if [ ! -z "${TARGET_HOST}" ] && [ ! -z "${USERS}" ] && [ ! -z "${SPAWNRATE}" ] && [ ! -z "${TIME}" ]; then
    echo "Running locust in headless mode"
    locust --headless --users "${USERS}" --spawn-rate "${SPAWNRATE}" -t "${TIME}" -H "${TARGET_HOST}" -f src/locustfile.py
else
    echo "Running locust with web interface"
    locust -f src/locustfile.py
fi
