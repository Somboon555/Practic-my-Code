#include <iostream>
using namespace std;
int main(){
    int x = 1 ,y = 2;
   
    bool z1 = x == y;
    cout << z1 << endl;
    
    bool z2 = x != y;
    cout << z2 << endl;
    
    bool z3 = x <= y;
    cout << z3 << endl;
    
    bool z4 = x >= y;
    cout << z4 << endl;
 
    bool z5 = x < y;
    cout << z5 << endl;
   
    bool z6 = x > y;
    cout << z6 << endl;
}
//C++ ไม่อนุญาตให้ประกาศตัวแปรชื่อเดียวกันซ้ำในขอบเขตเดียวกัน (scope เดียวกัน)