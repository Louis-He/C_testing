Remove-Item .\test.exe
g++ -o test sample.c main.cpp 
Get-Content .\input.in | .\test.exe > output.out