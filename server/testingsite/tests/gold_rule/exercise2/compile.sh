echo "[info] Removing old executable..."
rm test
g++ -o test sample.c main.cpp
echo "[info] Golden rule compile succeeded."
