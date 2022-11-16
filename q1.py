# https://www.youtube.com/watch?v=nj3StxDTvis
# Taking input from the user
# n = input()

str1 = "acad"
str2 = "academic"


z = len(str2)
for i in range(0, z):
    str1 += str1
for i in range(z, 8):
    str1 += str1

if (str1 == str2):
    print("YES")
else:
    print("NO")



# ##C++ code for refrence purpose#include <iostream>
# using namespace std;

# int main(){
# int t;
# cin>>t;
# while(t--){
# int n;
# cin>>n;
# string s;
# cin>>s;
# string str1,str2;
# for(int i=0;i<n/2;i++)
# str1+=s[i];
# for(int i=n/2;i<n;i++)
# str1+=s[i];
# if(str1==str2)
# cout<<"YES"<<endl;
# else;
# cout<<"NO"<<endl;


# }
# return 0;

# }

