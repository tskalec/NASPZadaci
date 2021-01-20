#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <limits>
#include <sstream>

uint32_t calculateDistance(const std::string &s1, const std::string &s2, uint16_t insertCost,
                           uint16_t deleteCost, uint16_t modifyCost) {
    size_t n = s1.size() + 1, m = s2.length() + 1;
    std::vector<uint32_t> dp(n * m, 0);
    for (size_t i = 0; i < m; i++) dp[0 + i] = insertCost * i;
    for (size_t i = 0; i < n; i++) dp[i*m + 0] = deleteCost * i;

    for (size_t i = 1; i < n; i++) {
        for (size_t j = 1; j < m; j++) {
            uint32_t currMin = std::numeric_limits<uint32_t>::max();
            currMin = std::min(currMin, dp[(i - 1) * m + j] + deleteCost);
            currMin = std::min(currMin, dp[i * m + j - 1] + insertCost);
            currMin = std::min(currMin, dp[(i - 1) * m + j - 1] + ((s1[i-1] == s2[j-1]) ? (uint32_t)0 : modifyCost));
            dp[i * m + j] = currMin;
        }
    }

    return dp[n * m - 1];
}

std::vector<std::string> splitBySpace(const std::string &sentence) {
    std::vector<std::string> result;
    std::stringstream ss(sentence);
    std::string word;
    while (ss >> word) {
        result.push_back(word);
    }
    return result;
}


std::pair<std::string, uint32_t> correctSentence(const std::string &sentence,
                                                 const std::set<std::string> &dictionary,
                                                 uint16_t insertCost, uint16_t deleteCost, uint16_t modifyCost) {
    std::vector<std::string> words = splitBySpace(sentence);
    std::vector<std::string> correctedWords;
    uint32_t totalCost = 0;

    for (std::string &word : words) {
        if (dictionary.count(word) > 0) {
            correctedWords.push_back(word);
        } else {
            std::pair<uint32_t, std::string> minCostWord = std::make_pair(std::numeric_limits<uint32_t>::max(), "");
            for (const auto &possibleWord : dictionary) {
                uint32_t currentCost = calculateDistance(word, possibleWord, insertCost, deleteCost, modifyCost);
                if (currentCost < minCostWord.first) {
                    minCostWord = std::make_pair(currentCost, possibleWord);
                }
            }
            correctedWords.push_back(minCostWord.second);
            totalCost += minCostWord.first;
        }
    }

    std::string correctSentence = correctedWords[0];
    for (size_t i = 1; i < correctedWords.size(); i++) {
        correctSentence.append(" " + correctedWords[i]);
    }
    return std::make_pair(correctSentence, totalCost);
}



int main() {
    uint16_t insertCost, deleteCost, modifyCost;
    std::string text;
    std::set<std::string> dictionary;

    std::getline(std::cin, text);
    std::cin >> insertCost >> deleteCost >> modifyCost;
    int numDict;
    std::cin >> numDict;
    for (int i = 0; i < numDict; i++) {
        std::string s;
        std::cin >> s;
        dictionary.insert(s);
    }

    auto result = correctSentence(text, dictionary, insertCost, deleteCost, modifyCost);
    std::cout << result.second << "\n" << result.first << std::endl;
}
