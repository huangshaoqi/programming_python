import re
import pprint

code = []
with open('source.txt') as f:
    content = f.read()
    patten_str = '<code class="xref">.*</code>'
    m1 = re.findall(patten_str, content)
    # print(m1)
    patten_str1 = '>(.*)<'
    for var in m1:
        m2 = re.findall(patten_str1, var)
        code.append(m2[0])

pprint.pprint(code)
print("Total: %s" % len(code))
