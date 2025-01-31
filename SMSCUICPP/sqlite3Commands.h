#ifndef SQLITE3COMMANDS_H
#define SQLITE3COMMANDS_H

#include <string>

int openDatabase();
void createTable();
void insertRecord(int id, const std::string &name, double finalGrade);
void deleteRecord(int id);
void searchRecordByID(int id);
void displayAllStudentRecords();


#endif