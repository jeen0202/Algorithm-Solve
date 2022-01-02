#include <string>
#include <vector>
#include <unordered_set>
#include <queue>
#include <iostream>
using namespace std;
typedef long long int ll;
unordered_set<ll> mem;
inline ll conv(vector<int> &stones){
    ll res = 0;
    for (int x: stones) res = res * 25 + x;
    return res;
}
string dfs(vector<int> stones, int k, string path) {
    mem.insert(conv(stones));
    // 종료 조건 (k개 남은 돌무더기 하나만 있는가?)
    int cnt_k = 0, cnt_zero = 0;
    for (int x: stones) {
        if (x == k) cnt_k++;
        if (x == 0) cnt_zero++;
    }
    if (cnt_zero == stones.size() - 1 && cnt_k == 1) return path;
    // 완전 탐색
    // 처음 찾은 방법이 사전 순으로 마지막임을 보장하기 위해 역순 탐색
    for (int i = stones.size() - 1; i >= 0; i--) {
        bool flag = true;
        stones[i] += 2;
        for (int &x: stones){
            x--;
            if (x < 0) flag = false;
        }
        if (flag && mem.find(conv(stones)) == mem.end()) {
            string res = dfs(stones, k, path + (char)(i + '0'));
            if (res != "-1") return res;
        }
        stones[i] -= 2;
        for (int &x: stones){
            x++;
        }
    }
    return "-1";
}
string solution(vector<int> stones, int k) {
    int sum = 0, n = stones.size();
    for (int x: stones) sum += x;
    if (n > 2 && (sum - k) % (n - 2) != 0) return "-1";
    if (sum < k) return "-1";
    return dfs(stones, k, "");
}

int main () {
    vector<int> stones = {1,3,2};
    cout << solution(stones,3) << endl;
}