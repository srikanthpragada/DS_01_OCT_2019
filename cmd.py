# coding: utf-8
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('lsmagic', '')
get_ipython().run_line_magic('system', 'dir')
cmds = get_ipython().run_line_magic('system', 'dir')
cmds
type(cmds)
lines = get_ipython().run_line_magic('system', 'dir')
type(lines)
for line in lines[:5]:
    print(line)
get_ipython().run_line_magic('system', "type 'e:\\classroom\\names.txt'")
