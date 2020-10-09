echo "[info] Removing old executable..."
rm test
echo "[info] Compiling new executable..."
g++ -o test sample.c main.cpp
echo "[info] Generate output file..."
./test < input.in > output.out
echo "[info] Output generated. Please submit through http://ctest.siweihe.tech/exercise/1 for testing."
