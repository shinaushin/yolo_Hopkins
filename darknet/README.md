# Adapted from darknet by pjreddie

1. Make a new branch: git checkout -b <new_branch>

2. Navigate into darknet directory

3. make clean

4. make

5. ./darknet detector train cfg/obj.data cfg/HopkinsAI-tiny.cfg -gpus 0,1 (because you have two GPUs if I remember correctly)

The program will save checkpoint weights every 100 iterations from iterations 0-1000, and after that, it'll save checkpoints weights every 1000 iterations.

It'll also output stats about the network every iteration (or every batch of iterations...don't remember exactly). And so depending on what the stats are once the training is all done, we can either call it done or extend the training from the last saved chcekpoint.

If you come across any errors, let me know, and I can help you debug.
