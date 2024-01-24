#include <iostream>
#include <string>

using namespace std;


int main(){
    std::string s1, s2, cur;
    std::cin >> s1;
    std::cin >> s2;
    s1 = std::sort(s1, s1.length());
    vector <string> count;
    for(int i = 0; i < s2.length()-s1.length(); i++){
        cur = s2.substr(i, s1.length());
        if(sort(cur, cur.length()) == s1){
            count.push_back(cur);
        }
    }
    std::cout << count.size();
    return 0;
}