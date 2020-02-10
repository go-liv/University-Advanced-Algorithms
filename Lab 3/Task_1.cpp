#include <iostream>
#include <string.h>
#include <vector>
#include <sstream>
#include <iterator>

std::string mirrorStr(std::string str)
{
    std::string word;
    std::string mirrored;

    std::istringstream strStream(str, std::istringstream::in);

    while(strStream >> word)
    {  
        int length = (int)std::distance(std::begin(word), std::end(word));

        if(word == )

        for(int i = 0; i < (length/2); i++)
        {
            char swap = word[i];
            word[i] = word[length - 1];
            word[length - 1] = swap;
        }

        mirrored.append(word + " ");
    }

    return mirrored;
}

int main()
{
    std::string str = "day time you is";
    
    std::cout << mirrorStr(str) << std::endl;
    return 0;
}