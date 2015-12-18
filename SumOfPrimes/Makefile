SumOfPrimes : SumOfPrimes.o
	g++ -Wall -o SumOfPrimes SumOfPrimes.o

SumOfPrimes.o : SumOfPrimes.cpp ../ConvenientHeaderFiles/sumOfVector.h ../ConvenientHeaderFiles/returnVectorOfPrimes.h ../ConvenientHeaderFiles/isPrime.h ../ConvenientHeaderFiles/printVector.h ../ConvenientHeaderFiles/largeSumOfIntVector.h
	g++ -Wall -c -std=c++11 SumOfPrimes.cpp

clean:
	rm SumOfPrimes SumOfPrimes.o
