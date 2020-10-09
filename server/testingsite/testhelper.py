def locate_next_case(text, current_line):
    while(current_line < len(text) and text[current_line].find('=== Case #') == -1):
        current_line += 1
    if(current_line >= len(text)):
        return -1
    else:
        return current_line