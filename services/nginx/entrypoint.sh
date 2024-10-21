#!/bin/bash

nginx -g 'daemon off;' &

promtail -config.file /etc/promtail/promtail-config.yaml &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
