#include <iostream>
#include <map>
using namespace std;

int numJewelsInStones(string J, string S)
{
    map<char, int> mp;
    int count = 0;
    for (auto c : S)
        mp[c]++;
    for (auto x : J)
        count += mp[x];

    return count;
}

int main(int argc, char const *argv[])
{
    string S, J;
    cin >> S >> J;
    cout << numJewelsInStones(S, J) << endl;
    return 0;
}
