def kmp_search(string, substring):
    """
    search substring in string using longest proper prefix list
    :param string: string to find in
    :param substring: substring to find in string
    :return: list of tuples with index of start position of substring and last if finds, else empty list
    """
    lps = form_lps(substring)
    result = []
    string_iterator = 0
    substring_iterator = 0
    while string_iterator < len(string):
        if substring[substring_iterator] == string[string_iterator]:
            string_iterator += 1
            substring_iterator += 1
            if substring_iterator == len(substring):
                result.append((string_iterator - substring_iterator, string_iterator - 1))
                substring_iterator = lps[substring_iterator - 1]
        elif substring_iterator != 0:
            substring_iterator = lps[substring_iterator - 1]
        else:
            string_iterator += 1
    return result


def form_lps(substring):
    """
    forms lps (longest proper prefix) list for holding the longest prefix suffix values for substring
    :param substring: string to form lps list from
    :return: list for holding the longest prefix suffix values for substring
    """
    lps = [0] * len(substring)
    iterator = 1
    match_index = 0
    while iterator < len(substring):
        if substring[iterator] == substring[match_index]:
            match_index += 1
            lps[iterator] = match_index
            iterator += 1
        elif match_index != 0:
            match_index = lps[match_index - 1]
        else:
            lps[iterator] = 0
            iterator += 1
    return lps
