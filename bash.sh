echo "starting Bot ~@DroneBots";
echo $PORT
kill -9 $(lsof -t -i:$PORT)
nohup python3 webApp.py > save_pid.txt >&1 &
# lsof -t -i:8082   
# kill -9 $(lsof -t -i:8082)
python3 -m main
