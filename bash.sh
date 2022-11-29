echo "starting Bot ~@DroneBots";
nohup python3 webApp.py > save_pid.txt >&1 &
# lsof -t -i:8082   
# kill -9 $(lsof -t -i:8082)
python3 -m main
