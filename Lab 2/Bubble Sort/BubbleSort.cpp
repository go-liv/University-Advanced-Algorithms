#include <iostream>
#include <vector>

std::vector<int> Swap(int x, int y, std::vector<int> array)
{
    int swap1 = array[x];
    int swap2 = array[y];
    
    array[x] = swap2;
    array[y] = swap1;

    return array;
}

std::vector<int> bubbleSort(std::vector<int> array)
{
    bool swap = true;
    while(swap == true)
    {
        swap = false;
        for(int i = 0; i < array.size()-1; i++)
        {
            if(array[i] > array[i+1])
            {
                swap = true;
                array = Swap(i, i+1, array);
            }
        }
    }

    return array;
}

int main()
{
    std::vector<int> array = {32, 553, 64, 1, 3859, 1245634, 2, 69, 1337, 420, 422};

    for(int i = 0; i < array.size(); i++)
    {
        std::cout << bubbleSort(array)[i] << std::endl; 
    }

    return 0;
}