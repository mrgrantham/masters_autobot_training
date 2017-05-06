
# run tail -f in background
tail -n 100 -F ../autobot_googlenet/autobot_googlenet_train_cp.log.train > awk '{print $1 " " $3 " " $4}' | feedgnuplot --lines --points --legend 0 "Learning Rate" --legend "Loss Rate" --title "Model Learning and Loss" --y2 2 --terminal 'dumb 120,35' --domain --nodataid --xlabel 'Time Elapse (Seconds)'  &

# process id of tail command
tailpid=$!

# wait for sometime
sleep 10

# now kill the tail process
kill $tailpid


