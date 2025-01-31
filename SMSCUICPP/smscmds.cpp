#include <iostream>
#include <limits>
#include <cctype>
#include "sqlite3Commands.h"

/* Helper function to validate name field. */
bool isAlpha(const std::string& str) {
    if (str.empty()){
        return false;
    }
    for (unsigned char c : str) {
        if (!isalpha(c) && c != ' '){ 
            return false;
        }
    }
    return true;
}

void addStudentRecord()
{
    /* This Student Management System will have 3 default fields in a student table (you may add more by modifiying source code):
     * Full Name --- > Must be made of alphabetical characters
     * Student ID (Primary Key) --- > Numeric only
     * Final Grade (Can be final grade for full year or semester wise data.) ---> Numeric only
     */

    std::string fullName {};
    int id {};
    double finalGrade {};

    while(true){
        std::cout << "Enter the students full name: " << "\n";
        std::getline(std::cin >> std::ws, fullName);

        if (!isAlpha(fullName)){
            fullName.clear();
            std::cout << "Invalid student name! Please enter a valid student name.\n";
        } else {
            break;
        }

    }


    while (true){
        std::cout << "Enter student ID: ";
        std::cin >> id;

        if(std::cin.fail()) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid student ID! Please enter a valid numeric student ID.\n";
        } else {
            break;
        }
    }

    while(true){
        std::cout << "Enter students final grade: ";
        std::cin >> finalGrade;

        if (std::cin.fail()) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid student grade! Please enter a valid numeric grade.\n";
        } else if (finalGrade < 0 || finalGrade > 100) {
            std::cout << "Invalid grade! Please enter a grade between 0 and 100.\n";
        } else {
            break;
        }
    }

    insertRecord(id,fullName,finalGrade);
         
}

/* Delete student record based on ID*/
void deleteStudentRecord()
{
    int id {};

    while (true){
        std::cout << "Enter students ID to delete connected record: ";
        std::cin >> id;

        if(std::cin.fail()) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid student ID! Please enter a valid numeric student ID.\n";
        } else {
            break;
        }
    }

    deleteRecord(id);

}

/* Search a student record by ID. */
void searchStudentRecord(){
    int id {};

    while (true){
        std::cout << "Enter students ID to search for record: ";
        std::cin >> id;

        if(std::cin.fail()) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid student ID! Please enter a valid numeric student ID.\n";
        } else {
            break;
        }
    }

    searchRecordByID(id);

}

void seeAllStudentRecords(){
    displayAllStudentRecords();
}


