from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

import random
import os
import re
from testhelper import *

from datetime import datetime
# Create your views here.


def index(request):
    return render(request, "tests/index.html")


def exercise(request, exercise_id):
    if request.method == 'POST':
        if request.FILES:
            try:
                in_file = request.FILES['in_file']
                out_file = request.FILES['out_file']
            except:
                return render(request, "tests/testerror.html", context={"reason": "[ERROR] Either input or output file not submitted."})

            in_text = ''
            out_text = ''
            for line in in_file:
                in_text = in_text + line.decode(encoding="utf-8")

            try:
                out_text = ''
                for line in out_file:
                    out_text = out_text + line.decode(encoding="utf-8")
            except:
                out_text = ''
                for line in out_file:
                    out_text = out_text + line.decode(encoding="utf-8-sig")

            print("[info] user input file loaded")

            # store input to a tmp file and run the gold rule to collect reference solution
            with open('tmp_input.txt', 'w') as tmp_in:
                tmp_in.write(in_text)
            result = os.popen(
                '~/testing_tool/tests/gold_rule/exercise' + str(exercise_id) + '/test < tmp_input.txt').read()

            out_text = out_text.replace('\r', '')
            out_text = out_text.split('\n')
            gold_text = result.split('\n')

            if len(out_text) == 0 or len(gold_text) == 0:
                return render(request, "tests/testerror.html", context={"reason": "[ERROR] Output file Empty."})

            test_num_out = int(out_text[0][out_text[0].find(
                '=== Test Number: ') + len('=== Test Number: '): -len(" ===")])
            test_num_gold = int(gold_text[0][gold_text[0].find(
                '=== Test Number: ') + len('=== Test Number: '): -len(" ===")])

            if test_num_out != test_num_gold:
                return render(request, "tests/testerror.html", context={"reason": "[ERROR] Output file either has more test cases or less test cases than it should have."})

            # try:
            current_line_gold = 1
            current_line_out = 1
            current_id = 1
            result = [0 for i in range(test_num_gold + 1)]
            while(current_id != test_num_gold + 1):
                # if WA in the middle of the case
                if gold_text[current_line_gold] != out_text[current_line_out]:
                    # print('test')
                    result[current_id] = -1
                    # skip all the way to the next case
                    current_line_out = locate_next_case(
                        out_text, current_line_out)
                    current_line_gold = locate_next_case(
                        gold_text, current_line_gold)

                    if(current_line_gold == -1):
                        current_id = test_num_gold + 1
                    else:
                        next_id = int(
                            gold_text[current_line_gold][
                                gold_text[current_line_gold].find('=== Case #') + len('=== Case #'): -len(" ===")])
                        current_id = next_id
                    continue

                # if gold solution end
                if gold_text[current_line_gold].find('=== Case #') != -1:
                    next_id = int(
                        gold_text[current_line_gold][gold_text[current_line_gold].find('=== Case #') + len('=== Case #'): -len(" ===")])

                    # gold solution end, user solution not end, WA
                    if out_text[current_line_out].find('=== Case #') == -1:
                        result[current_id] = -1
                        current_line_out = locate_next_case(
                            out_text, current_line_out)
                    else:
                        result[current_id] = 1

                    current_id = next_id

                # print(current_line_gold, current_line_out)
                current_line_gold += 1
                current_line_out += 1

                if(current_line_gold >= len(gold_text)):
                    if(current_line_out >= len(out_text)):
                        result[current_id] = 1
                    else:
                        result[current_id] = -1
                    break

            passed = result.count(1)
            failed = result.count(-1)
            pass_rate = round(passed / test_num_gold * 100, 1)
            # TO_DO: check user output and gold rule output
            return render(request, "tests/result.html", context={"results": result[1:], "passed": passed, "failed": failed, "pass_rate": pass_rate})
            # except:
            #     return render(request, "tests/result.html", context={"reason": "[ERROR] Internal Error Occured."})
        else:
            return render(request, "tests/testerror.html", context={"reason": "[ERROR] No file submitted."})
    else:
        if exercise_id == 1 or exercise_id == 2:
            return render(request, "tests/testpage.html", context={"exercise_id": exercise_id})
        else:
            return render(request, "tests/testinprogress.html")


def input(request, exercise_id):
    input_file = ""
    if exercise_id > 2:
        return render(request, "tests/testinprogress.html")
    if exercise_id == 1:
        case = 50
        input_file += str(case) + "\n"
        for i in range(case):
            input_file += str(i + 1) + "\n" + \
                str(random.randrange(-32677, 32768, 1)) + "\n"
    elif exercise_id == 2:
        auto_case = 30
        corner_case = 5
        input_file += str(auto_case + corner_case) + "\n"
        for i in range(auto_case):
            timestamp_1 = datetime.fromtimestamp(
                random.randrange(0, 2000000000, 1))
            timestamp_2 = datetime.fromtimestamp(
                random.randrange(0, 2000000000, 1))

            input_file += str(i + 1) + "\n" + \
                timestamp_1.strftime("%Y %m %d %H %M %S") + "\n" + \
                timestamp_2.strftime("%Y %m %d %H %M %S") + "\n"

        input_file += "31\n" + \
            "1968 01 01 00 00 00\n" + \
            "2017 02 03 01 02 03\n"

        input_file += "32\n" + \
            "2017 01 01 00 00 00\n" + \
            "1968 02 03 01 02 03\n"

        input_file += "33\n" + \
            "2000 02 29 00 00 00\n" + \
            "1997 12 03 01 02 03\n"

        input_file += "34\n" + \
            "2000 13 29 00 00 00\n" + \
            "2009 12 32 01 02 03\n"

        input_file += "35\n" + \
            "1998 02 29 03 00 00\n" + \
            "1999 06 17 24 61 61\n"

    return HttpResponse(input_file, content_type="text/plain")


def skeleton(request, exercise_id, platform):
    if exercise_id <= 2 and exercise_id > 0:
        filename = 'exercise' + str(exercise_id) + '_' + platform + '.zip'
        filepath = "/ctest/exercise" + \
            str(exercise_id) + "/" + platform + "/" + filename
        print(filepath)
        response = HttpResponse()
        response["Content-Disposition"] = "attachment; filename=" + filename
        response['X-Accel-Redirect'] = filepath
        return response
    return None


def syllabus(request):
    return render(request, "tests/syllabus.html")


def cookbook_index(request, section):
    return render(request, "tests/cookbook/cookbook_" + section + ".html")
