echo "[info] Removing old executable..."
Remove-Item .\test.exe
echo "[info] Compiling new executable..."
g++ -o test sample.c main.cpp
echo "[info] Generate output file..."
Get-Content .\input.in | .\test.exe | Out-File -Encoding utf8 output.out
echo "[info] Output generated. Please submit through http://ctest.siweihe.tech/exercise/2 for testing."
