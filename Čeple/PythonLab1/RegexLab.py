import re

num_re = re.compile(r'(\([BR]\))([0-9]+)')

one_digit = re.compile(r'(\([BR]\))(\d)')
two_digits = re.compile(r'(\([BR]\))(\d{2})')
three_digits = re.compile(r'(\([BR]\))(\d{3})')


def repl_fun(matchobj) -> str:
    cap_num = matchobj.group(2)
    # Process here - pad the number with zeroes
    if len(cap_num) > 4:
        raise ValueError("Length of a value is greater than 4!")

    while len(cap_num) < 4:
        cap_num = "0" + cap_num
    return matchobj.group(1) + cap_num


with open('regLabExp1', 'r') as src:
    with open('regLabExp1_Result', 'w') as dst:
        for line in src.readlines():
            to_write_line = line
            if not line.startswith("test_tree.add_node"):
                # First do the regex sub, then write to file
                to_write_line = num_re.sub(repl_fun, to_write_line)

            dst.write(to_write_line)
