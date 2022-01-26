/// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// Title: Cipher_Code_Decryption.cpp 
// course: Computational Problem Solving I (CPET-121)
// Developer: Miftahul Huq (Freshmen at RIT) 
// Date: 08/07/2020
// Description: The following code decrypts (decode) a message that was
//              encoded using a variation of the Baconian Chipher. Each file
//              contians a phrase, and with them contains a hidden message
//              based on the capitalization of the letters message. The 
//              below code can seperately decode the hidden message that is
//              within them.
// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

using namespace std;

// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// Name: nonAlphaChecker()
// Input: (1) Call-by-reference string variable and file
// Output: (1) String withoug any nonalphabet letters
// Purpose: Take any nonalphabet letters from the user string
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
string nonAlphaChecker(string& userString, ifstream& inFile) {
  char data;
  inFile.get(data);
  while (!inFile.eof()) {
    if (isalpha(data)) {
      userString.push_back(data); // Adds the character
    }
    inFile.get(data);
  }
  return userString;
}

// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// Name: messageDecoder()
// Input: (1) String variable
// Output: (1) String
// Purpose: decode the string according to the Cipher Code Decryption 
// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
void messageDecoder (string userString) {
  unsigned i;
  string encodedLetters;
  string substring;
  
  /* code below doesn't use the last 4 character and 
  make use of what the code can use */
  while (userString.size() >= 5) { 
    substring = userString.substr(0, 5);
    userString.erase(0, 5);//Delets the 5 character that in use
    for (i = 0; i < 5; ++i) {
      if (isupper(substring.at(i))) {
        encodedLetters.push_back('U');
      }
      else {
        encodedLetters.push_back('L');
      }
    }

    if (encodedLetters == "UUUUU") {
      cout << 'A';
    }
    else if (encodedLetters == "UUUUL") {
      cout << 'B';
    }
    else if (encodedLetters == "UUULU") {
      cout << 'C';
    }
    else if (encodedLetters == "UUULL") {
      cout << 'D';
    }
    else if (encodedLetters == "UULUU") {
      cout << 'E';
    }
    else if (encodedLetters == "UULUL") {
      cout << 'F';
    }
    else if (encodedLetters == "UULLU") {
      cout << 'G';
    }
    else if (encodedLetters == "UULLL") {
      cout << 'H';
    }
    else if (encodedLetters == "ULUUU") {
      cout << 'I';
    }
    else if (encodedLetters == "ULUUL") {
      cout << 'J';
    }
    else if (encodedLetters == "ULULU") {
      cout << 'K';
    }
    else if (encodedLetters == "ULULL") {
      cout << 'L';
    }
    else if (encodedLetters == "ULLUU") {
      cout << 'M';
    }
    else if (encodedLetters == "ULLUL") {
      cout << 'N';
    }
    else if (encodedLetters == "ULLLU") {
      cout << 'O';
    }
    else if (encodedLetters == "ULLLL") {
      cout << 'P';
    }
    else if (encodedLetters == "LUUUU") {
      cout << 'Q';
    }
    else if (encodedLetters == "LUUUL") {
      cout << 'R';
    }
    else if (encodedLetters == "LUULU") {
      cout << 'S';
    }
    else if (encodedLetters == "LUULL") {
      cout << 'T';
    }
    else if (encodedLetters == "LULUU") {
      cout << 'U';
    }
    else if (encodedLetters == "LULUL") {
      cout << 'V';
    }
    else if (encodedLetters == "LULLU") {
      cout << 'W';
    }
    else if (encodedLetters == "LULLL") {
      cout << 'X';
    }
    else if (encodedLetters == "LLUUU") {
      cout << 'Y';
    }
    else if (encodedLetters == "LLUUL") {
      cout << 'Z';
    }
    else if (encodedLetters == "LLULU") {
      cout << '.';
    }
    else if (encodedLetters == "LLULL") {
      cout << ';';
    }
    else if (encodedLetters == "LLLUU") {
      cout << '!';
    }
    else if (encodedLetters == "LLLUL") {
      cout << '?';
    }
    else if (encodedLetters == "LLLLU") {
      cout << '0';
    }
    else if (encodedLetters == "LLLLL") {
      cout << ' ';
    }

    // Delets the letters to append new ones during this loop
    encodedLetters.erase(0, 5); 
  }
}

int main() {
  string userString;
  ifstream inFile;
  string userInput;

  cin >> userInput;
  inFile.open(userInput.c_str());

  if (!inFile.is_open()) {
    cout << "DATA FILE DID NOT OPEN... Program Terminated";
    exit(1); // Terminated code if the file  cannot be opened
  }
  else {
    nonAlphaChecker(userString,inFile);
    messageDecoder(userString);
  }

  inFile.close();

  return 0;
}
