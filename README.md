# HOW WATCHFILES WORKS
https://watchfiles.helpmanual.io/#how-watchfiles-works


# RUNNING COMMAND
## On Server
cd /home/ubuntu/script
python3 watch_push_restart.py <remote_ip> <port_ssh> ubuntu "/home/ubuntu/.ssh/id_ed25519" "/home/ubuntu/config"
nano ../config/url_hub/.env
tail -f logs/app.log
### PID: if running in background
ps ax | grep watch_push_restart.py
kill -9 PID