NAME=autobot_objdetector
CC=g++
SRC=autobot_objdetector.cpp

CFLAGS=

all:
	$(CC) `pkg-config --cflags --libs opencv` $(SRC) -o $(NAME)

LinuxAll:
	$(CC) -L/usr/local/lib $(SRC) -o $(NAME) -lopencv_core -lopencv_imgproc -lopencv_videoio -lopencv_imgcodecs -lopencv_objdetect -lopencv_features2d -lopencv_highgui

clean:
	rm $(NAME)
