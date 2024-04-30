# Leetcode - 1678

def interpret(command):
    # print(command.spli)
    return command.replace("()","o").replace("(al)","al")

print(interpret("G()()(al)"))
