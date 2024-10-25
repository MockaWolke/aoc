#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <queue>

#define FILE_NAME "test_input.txt"
#define N_MONKEYS 4
// #define FILE_NAME "input.txt"
// #define N_MONKEYS 8

using namespace std;
typedef unsigned long long int ulli;

ifstream infile(FILE_NAME);
queue<ulli> startingItems;
vector< queue<ulli> > monkeyStartingItems(N_MONKEYS, startingItems);
bool valueRiseOperation[N_MONKEYS];  // true==multiplication, false==addition
int valueRiseBy[N_MONKEYS];
int throwTo[N_MONKEYS][2];  // i==0 -> true , i==1 -> false
int divisionTestBy[N_MONKEYS];
int inspectCounts[N_MONKEYS] = {0};


void parseInput() {
    int iMonkey = 0;
    string currentLine;
 
    while(getline(infile, currentLine)) {
        if (!currentLine.empty()) {
            if (currentLine.length() >= 16 && currentLine.at(16) == ':') {
                string itemValues = currentLine.substr(18);
                int itemStart = 0;
                for (int i=0; i<itemValues.length(); i++) {
                    if (itemValues.at(i) == ',' || i == itemValues.length()-1) {
                        monkeyStartingItems[iMonkey].push(stoi(itemValues.substr(itemStart, i+1)));
                        itemStart = i+1;
                    }
                }
            } else if (currentLine.length() > 23 && currentLine.at(23) == '*') {
                valueRiseOperation[iMonkey] = true;
                if (currentLine.substr(25) != "old") {
                    valueRiseBy[iMonkey] = stoi(currentLine.substr(25));
                } else {
                    valueRiseBy[iMonkey] = -1000;
                }
            } else if (currentLine.length() > 23 && currentLine.at(23) == '+') {
                valueRiseOperation[iMonkey] = false;
                if (currentLine.substr(25) != "old") {
                    valueRiseBy[iMonkey] = stoi(currentLine.substr(25));
                } else {
                    valueRiseBy[iMonkey] = -1000;
                }
            } else if (currentLine.length() > 19 && currentLine.at(19) == 'y') {
                divisionTestBy[iMonkey] = stoi(currentLine.substr(20));
            } else if (currentLine.substr(7,3) == "tru") {
                throwTo[iMonkey][0] = currentLine.at(currentLine.length()-1) - '0';
            } else if (currentLine.substr(7,3) == "fal") {
                throwTo[iMonkey][1] = currentLine.at(currentLine.length()-1) - '0';
            }
        } else {
            iMonkey++;
        }
    }
}

void playRounds(int nRounds, int part) {
    int prodDivisionTestBy = 1;
    for (int d=0; d<N_MONKEYS; d++) {
        prodDivisionTestBy *= divisionTestBy[d];
    }
    for (int r=0; r<nRounds; r++) {
        for (int i=0; i<N_MONKEYS; i++) {
            // cout << "Monkey: " << i << "\n";
            while (!monkeyStartingItems.at(i).empty()) {
                int currentItemValue = monkeyStartingItems.at(i).front();
                // cout << "  Inspects: " << currentItemValue << "\n";
                monkeyStartingItems.at(i).pop();
                int raiseBy;
                if (valueRiseBy[i] != -1000) {
                    raiseBy = valueRiseBy[i];
                } else {
                    raiseBy = currentItemValue;
                }
                if (valueRiseOperation[i]) {
                    currentItemValue *= raiseBy;
                } else {
                    currentItemValue += raiseBy;
                }
                if (part == 1) {
                    currentItemValue /= 3;
                    // cout << "    WorryLevel / 3= " << currentItemValue << "\n";
                } else {
                    currentItemValue = prodDivisionTestBy %currentItemValue;
                }
                if (currentItemValue % divisionTestBy[i] == 0) {
                    // cout << "    WorryLevel is dividible by " << divisionTestBy[iMonkey] << "\n";
                    // cout << "    Item thrown to " << throwTo[iMonkey][0] << "\n";
                    monkeyStartingItems.at(throwTo[i][0]).push(currentItemValue);
                } else {
                    // cout << "    WorryLevel is not dividible by " << divisionTestBy[iMonkey] << "\n";
                    // cout << "    Item thrown to " << throwTo[iMonkey][1] << "\n";
                    monkeyStartingItems.at(throwTo[i][1]).push(currentItemValue);
                }

                inspectCounts[i]++;
            }
        }
    }
}

int part1 () {
    parseInput();
    playRounds(20, 1);

    for (int i=0; i<N_MONKEYS; i++) {
        cout << "Monkey " << i << ": " << inspectCounts[i] << "\n";
    }

    return 0;
}

int part2 () {
    parseInput();
    playRounds(20, 2);

    for (int i=0; i<N_MONKEYS; i++) {
        cout << "Monkey " << i << ": " << inspectCounts[i] << "\n";
    }

    return 0;
}

int main() {
    part2();
    return 0;
}