compile:
	mkdir --parents bin build
	cython --embed main.py -o build/network_ping_log.c
	gcc -I /usr/include/python3.5 build/network_ping_log.c `python3.5-config --libs` -o bin/network_ping_log
clean:
	rm -r bin build
