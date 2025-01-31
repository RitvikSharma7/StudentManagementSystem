smsclicpp: smsSelectMenu.o smscmds.o sqlite3Commands.o sqlite3.o
	g++ -o smsclicpp smsSelectMenu.o smscmds.o sqlite3Commands.o sqlite3.o

smsSelectMenu.o: smsSelectMenu.cpp
	g++ -c smsSelectMenu.cpp

smscmds.o: smscmds.cpp smscmds.h
	g++ -c smscmds.cpp

sqlite3Commands.o: sqlite3Commands.cpp sqlite3Commands.h
	g++ -c sqlite3Commands.cpp

sqlite3.o: sqlite3.c sqlite3.h
	gcc -c sqlite3.c

run:
	./smsclicpp

clean:
	rm -f smsSelectMenu.o smscmds.o sqlite3Commands.o sqlite3.o smsclicpp sms.db
