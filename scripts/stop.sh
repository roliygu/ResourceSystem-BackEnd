#!/usr/bin/env bash

SPID=`ps aux | grep manage.py | grep -v grep | grep -v kill | awk '{print $2}'`

if [ -n "$SPID" ]; then
  kill ${SPID}
  while kill -9 ${SPID} 2>/dev/null; do echo "WebServer is shutting down..."; sleep 1; done
fi