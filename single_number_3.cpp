#include <bits/stdc++.h>
using namespace std;

vector<int> singleNumber(vector<int> &nums)
{
    int x, y, res(0);

    for (int i = 0; i < nums.size(); i++)
        res ^= nums[i];

    int t = res;
    int pos = 0;
    while (!(t & 1))
    {
        t >>= 1;
        pos++;
    }
    int mask = 1 << pos;

    x = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i] & mask)
            x ^= nums[i];
    }

    return vector<int>{x, res ^ x};
}
