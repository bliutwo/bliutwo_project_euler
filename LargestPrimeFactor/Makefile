# CFLAGS=-lm

# LIBS=-lm

LargestPrimeFactor : LargestPrimeFactor.o
	g++ -Wall -o LargestPrimeFactor LargestPrimeFactor.o

LargestPrimeFactor.o : LargestPrimeFactor.cpp sqrt.h FastInvSqrt.h
	g++ -Wall -c -std=c++11 LargestPrimeFactor.cpp

clean:
	rm LargestPrimeFactor LargestPrimeFactor.o
