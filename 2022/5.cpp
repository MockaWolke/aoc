#include <iostream>
#include <vector>
#include <fstream>
#include <regex>

using namespace std;

ifstream file("5.txt");
string str;
vector <string> stack_lines;
regex r("move ([0-9]+) from ([0-9]+) to ([0-9]+)");
smatch match;
vector <vector<int>> instructions;
vector <vector<char>> stacks;

string part_1(vector<vector<int>> instructions,vector<vector<char>> stacks){

    // iterate through instructions
    for (vector<vector<int>>::iterator it = instructions.begin(); it != instructions.end(); ++it){
        vector <int> ins = *it;
        int times = ins[0], from =  ins[1]-1,to = ins[2]-1;
        for (int i = 0; i < times; i++){
            stacks[to].push_back(stacks[from].back());
            stacks[from].pop_back();
        }
    }

    string result = "";
    for (int i = 0; i < stacks.size(); i++){
        result += stacks[i].back();
    }

    return result;
}


string part_2(vector<vector<int>> instructions,vector<vector<char>> stacks){

    // iterate through instructions
    for (vector<vector<int>>::iterator it = instructions.begin(); it != instructions.end(); ++it){
        vector <int> ins = *it;
        int times = ins[0], from =  ins[1]-1,to = ins[2]-1;

        vector <char> inter_med;

        for (int i = 0; i < times; i++){
            inter_med.push_back(stacks[from].back());
            stacks[from].pop_back();
        }

        for (int i = 0; i < times; i++){
            stacks[to].push_back(inter_med.back());
            inter_med.pop_back();
        }

        
    }

    string result = "";
    for (int i = 0; i < stacks.size(); i++){
        result += stacks[i].back();
    }

    return result;
}


int main(){
    while (getline(file,str)){
        if (str ==""){
            break;
        }
        stack_lines.push_back(str);
    }
    stack_lines.pop_back();

    reverse(stack_lines.begin(),stack_lines.end());

    int len_towers = (stack_lines[0].size()) /4 + 1;
    cout << len_towers << endl;

    for (int i = 0; i < len_towers;i++){
        stacks.push_back({});
    }

    for (vector<string>::iterator it = stack_lines.begin(); it != stack_lines.end(); ++it){

        int k = 0;
        string line = *it;
        for (int v = 1; v< line.size(); v=v+4){

            char c = char(line[v]);
            if (c!= ' '){
                stacks[k].push_back(c);
                }

            k++;
        }
    }

    while (getline(file,str)){
        regex_match(str,match,r);
        vector <int> new_isntruction;
    
        if (match.size()!=4){
            cout << "Error" << str << "!";
        }

        for (int i =1; i < match.size(); i++){
            new_isntruction.push_back( stoi(match[i].str()) );
        }

        instructions.push_back(new_isntruction);

    }

    cout << "Part 1: " << part_1(instructions,stacks) << endl;
    cout << "Part 2: " << part_2(instructions,stacks) << endl;

    return 1;
}