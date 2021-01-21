#include <iostream>
#include <random>
#include <set>

std::random_device rd;
std::mt19937 gen(rd());

std::string generateWord(int len) {
    std::string result;
    for (int i = 0; i < len; i++) {
        result += ('a' + gen()%26);
    }
    return result;
}

int main(int argc, char* argv[]) {
    int averageWordLen = std::atoi(argv[1]);
    int dictionarySize = std::atoi(argv[2]);
    int sentenceLength = std::atoi(argv[3]);
    int insertCost = std::atoi(argv[4]);
    int deleteCost = std::atoi(argv[5]);
    int modifyCost = std::atoi(argv[6]);

    std::normal_distribution<double> lenDist(averageWordLen, sentenceLength/10.0);
    std::set<std::string> dictionary;
    std::string sentence;

    while (dictionary.size() < dictionarySize) {
        int len = (int) std::max(0.0, lenDist(gen));
        std::string word = generateWord((int) std::max(0.0, lenDist(gen)));
        dictionary.insert(word);
    }
    for (int i = 0; i < sentenceLength; i++) {
        if (i > 0) sentence += " ";
        int len = (int) std::max(0.0, lenDist(gen));
        sentence += generateWord(len);
    }

    std::cout << sentence << "\n";
    std::cout << insertCost << " " << deleteCost << " " << modifyCost << "\n";
    std::cout << dictionarySize << "\n";
    for (std::string word : dictionary) {
        std::cout << word << std::endl;
    }
}
