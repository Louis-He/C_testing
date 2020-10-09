#include "sample.h"

#include <math.h>
#include <stdbool.h>
#include <stdio.h>

const int DAY_SECONDS = 24 * 60 * 60;
const int HOUR_SECONDS = 60 * 60;
const int MINUTE_SECONDS = 60;

void hello1() {
    int timestamp1 = get_timestamp();
    printf("%d\n", timestamp1);
    int timestamp2 = get_timestamp();
    printf("%d\n", timestamp2);
}

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

void convert_seconds_to_str(int time_difference) {
    int days, hours, minutes, seconds;

    days = time_difference / DAY_SECONDS;
    time_difference = time_difference - days * DAY_SECONDS;
    hours = time_difference / HOUR_SECONDS;
    time_difference = time_difference - hours * HOUR_SECONDS;
    minutes = time_difference / MINUTE_SECONDS;
    time_difference = time_difference - minutes * MINUTE_SECONDS;
    seconds = time_difference;

    if (days < 10) {
        printf("0%d day", days);
    } else {
        printf("%d day", days);
    }
    if (days > 1 || days == 0) {
        printf("s");
    }

    printf(", ");

    if (hours < 10) {
        printf("0%d hour", hours);
    } else {
        printf("%d hour", hours);
    }
    if (hours > 1 || hours == 0) {
        printf("s");
    }

    printf(", ");

    if (minutes < 10) {
        printf("0%d minute", minutes);
    } else {
        printf("%d minute", minutes);
    }
    if (minutes > 1 || minutes == 0) {
        printf("s");
    }

    printf(", ");

    if (seconds < 10) {
        printf("0%d second", seconds);
    } else {
        printf("%d second", seconds);
    }
    if (seconds > 1 || seconds == 0) {
        printf("s");
    }

    printf("\n");
}

int get_timestamp() {
    int year, month, date, hour, minute, second;
    scanf("%d", &year);
    scanf("%d", &month);
    scanf("%d", &date);
    scanf("%d", &hour);
    scanf("%d", &minute);
    scanf("%d", &second);

    int result = 0;
    // add all the years all the way up to year - 1
    if (year < 1970) {
        return -1;
    }
    for (int i = 1970; i < year; i++) {
        bool is_leap = is_leap_year(i);
        result += is_leap ? 366 * 24 * 60 * 60 : 365 * 24 * 60 * 60;
    }
    // add all the months all the way up to month - 1
    if (month <= 0 || month >= 13) {
        return -1;
    }
    for (int i = 1; i < month; i++) {
        result += get_month_day_num(year, i) * 24 * 60 * 60;
    }
    // add all the days all the way up to day - 1
    int max_day = get_month_day_num(year, month);
    if (date <= 0 || date > max_day) {
        return -1;
    }
    result += (date - 1) * 24 * 60 * 60;
    // add all the hours all the way up to hour - 1
    if (hour < 0 || hour > 23) {
        return -1;
    }
    result += hour * 60 * 60;
    // add all the minutes all the way up to minute - 1
    if (minute < 0 || minute > 59) {
        return -1;
    }
    result += minute * 60;
    // add all the seconds all the way up to second
    if (second < 0 || second > 59) {
        return -1;
    }
    result += second;

    return result;
}

int get_month_day_num(int year, int month) {
    bool is_leap = is_leap_year(year);
    switch (month) {
        case 1:
            return 31;
        case 2:
            return is_leap ? 29 : 28;
        case 3:
            return 31;
        case 4:
            return 30;
        case 5:
            return 31;
        case 6:
            return 30;
        case 7:
            return 31;
        case 8:
            return 31;
        case 9:
            return 30;
        case 10:
            return 31;
        case 11:
            return 30;
        case 12:
            return 31;
        default:
            return -1;
    }
}

bool is_leap_year(int year) {
    if (year % 400 == 0) {
        return true;
    } else if (year % 100 == 0) {
        return false;
    } else if (year % 4 == 0) {
        return true;
    } else {
        return false;
    }
}