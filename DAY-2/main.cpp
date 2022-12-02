//Advent of Code DAY-2 by Pierrafrom

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream Data(R"(C:\Users\pierr\OneDrive\programmes\Advent of Code\DAY-2\Part2\Data.txt)");

    string line;
    int score = 0;

    while (getline(Data, line))
    {
        if (line == "A X")
        {
            score += 3;
        }
        else
        {
            if (line == "A Y")
            {
                score += 4;
            }
            else
            {
                if (line == "A Z")
                {
                    score += 8;
                }
                else
                {
                    if (line == "B X")
                    {
                        score += 1;
                    }
                    else
                    {
                        if (line == "B Y")
                        {
                            score += 5;
                        }
                        else
                        {
                            if (line == "B Z")
                            {
                                score += 9;
                            }
                            else
                            {
                                if (line == "C X")
                                {
                                    score += 2;
                                }
                                else
                                {
                                    if (line == "C Y")
                                    {
                                        score += 6;
                                    }
                                    else
                                    {
                                        if (line == "C Z")
                                        {
                                            score += 7;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    cout << score << endl;


    return 0;
}
