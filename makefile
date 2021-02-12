all:	calculator
calculator:	calculator.cpp
	g++ -std=c++17 -g calculator.cpp -o calculator
