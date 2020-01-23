#include <iostream>
#include <string>


std::string joinStrings(std::string str1, std::string str2)
{
    //New string with joined result and iterator creation
    std::string joined = "";
    int i = 0;

    //This loop goes through all the characters of both strings until
    //it reaches the end of the smallest string
    for(i; i < str1.length(); i++)
    {
        joined += str1[i];
        joined += str2[i];
    }

    //If one of the strings is bigger, the part of that string that
    //is still not in joined will be appended to the end of joined
    if(i < str1.length())
        joined += str1.substr(i, str1.length());

    if(i < str2.length())
        joined += str2.substr(i, str2.length());        

    return joined;
}

int main()
{
    //Input Strings to merge
    std::string str1 = "";
    std::string str2 = "";

    //The func can also be called by inputing the 2 strings
    std::cout << "Tell me 2 words to join (separate them with spaces)" << std::endl;
    std::cin >> str1 >> str2;

    
    std::cout << joinStrings(str1, str2) << std::endl;
    return 0;
}