/* Arthor: Louis He
 * Year: 2020
 *
 * This file is for acedemic training purpose only. Do NOT distribute this file without the consent of the arthor.
 */

#include "sample.h"

#include <math.h>
#include <stdio.h>

/* hello1: code that will run to test part 1 of exercise 2
 * parameter: none
 * return: none
 */
void hello1() {
    int timestamp1 = get_timestamp();
    printf("%d\n", timestamp1);
    int timestamp2 = get_timestamp();
    printf("%d\n", timestamp2);
}

/* hello2: code that will run to test part 2 of exercise 2
 * parameter: none
 * return: none
 */
void hello2() {
    int timestamp1 = get_timestamp();
    int timestamp2 = get_timestamp();

    if (timestamp1 == -1 || timestamp2 == -1) {
        printf("Error: invalid inputs\n");
        return;
    }

    int time_difference = int(abs(timestamp2 - timestamp1));
    convert_seconds_to_str(time_difference);
}

/* convert_seconds_to_str: code that will convert time difference in seconds to a string
 * parameter: int: time_difference in seconds
 * return: none
 * output: print time difference in string using format {DD days, HH hours, MM minutes, SS seconds}
 */
void convert_seconds_to_str(int time_difference) {
    /* Please complete your code for part 1 here */
}

/* get_timestamp: code that will scanin datetime and return timestamp
 * parameter: none
 * return: integer represents timestamp
 */
int get_timestamp() {
    /* Please complete your code for part 2 here */
}
