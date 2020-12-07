class Solution(object):
    def __init__(self):
        self.res = ""
        self.index = 0
    def interpret(self, command):
        while self.index!=len(command):
            if (command[self.index]=='G'):
                self.res += "G"
            elif ((command[self.index]=='(')and(command[self.index+1]==')')):
                self.res += "o"
                self.index += 1
            else:
                self.res += "al"
                self.index += 3
            self.index += 1
        return self.res
