#include <iostream>
#include <vector>
using namespace std;

int singleNumber(vector<int> &nums)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int res = nums[0];

    for (int i = 1; i < nums.size(); i++)
    {
        res ^= nums[i];
    }
    return res;
}
