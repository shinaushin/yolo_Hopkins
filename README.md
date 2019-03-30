# yolo_Hopkins

1. Go into darknet directory
2. make clean
3. make
4. ./darknet detector train cfg/obj.data cfg/HopkinsAI-tiny.cfg -gpus 0,1 (because you have two GPUs if I remember correctly)

As it is training, it will save checkpoint weights for the network every 100 iterations from iter 0-1000. After that, it will save checkpoint weights every 1000 iterations.

It also outputs stats about the network, and so just let me know what the final stats are of the network. If they're not satisfactory, we can extend the training session by starting from the latest checkpoint. 

If you run into any errors, let me know. I'll try to debug them and let you know how to fix it.
