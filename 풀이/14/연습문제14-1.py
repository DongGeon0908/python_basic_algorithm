def get_name(s_info, find_no):
    if find_no in s_info:
        return s_info[find_no]
    else:
        return "?"

sample_info = {
    39: "justrin",
    14: "kim",
    67: "mike"
}

print(get_name(sample_info, 14))
