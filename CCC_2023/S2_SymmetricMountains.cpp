#include <iostream>
#include <climits>

using namespace std;

int main(){
    int n; cin >> n;
    int arr[n];
    int o[n];
    for(int i = 0; i < n; i++){
        cin >> arr[i];
        o[i] = INT_MAX;
    }
    int cur = 0;
    for (int i = 0; i < n; i++){
        cur = 0;
    
        // This takes care of odd widths
        for (int d = 0; d+i < n && i-d >= 0; d++){
            cur += abs(arr[i-d] - arr[i+d]);
            if (cur < o[d*2]){
                o[d*2] = cur;
            }
        }
        cur = 0;
        // // This takes care of even widths ( assuming i is left of center)
        for (int d = 1; d+i < n && i-d+1 >= 0; d++){
            cur += abs(arr[i-d+1] - arr[i+d]);
            if (cur < o[d*2-1]){
                o[d*2-1] = cur;
            }
        }

    }
    

    for (int i = 0; i < n; i++){
        cout << o[i] << ' ';
    }
    cout << endl;

}

/*
7
3 1 4 1 5 9 2
*/