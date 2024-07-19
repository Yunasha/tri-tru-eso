import sys

# !! RUN IN TERMINAL
if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <input file>")
    sys.exit(1)

file = [x.split(" ") for x in open(f"{sys.argv[1]}.tri", "r").readlines()]

data = []

for line in file:
    for word in line:
        data.append(word.split("\n")[0])
        data.append("ENL") if word[-1] == "\n" else ...

data.append("ENL") if data[-1] != "ENL" else ...

class Token:
    output: str = "OUT"
    text: str = "TXT"
    number: str = "NUM"
    endline: str = "ENL"
    newline: str = "NWL"
    end: str = "END"
    variable: str = "VAR"
    flag: str = "FLG"
    jump: str = "JPT"
    jump_zero: str = "JPZ"
    jump_positive: str = "JPP"
    jump_negative: str = "JPN"
    space: str = "SPC"
    add: str = "ADD"
    subtract: str = "SUB"
    multiply: str = "MUL"
    divide: str = "DIV"
    modulo: str = "MOD"
    copy: str = "CPY"
    read: str = "RED"


    tokens = [
        "",
        output,
        text,
        number,
        endline,
        newline,
        end,
        variable,
        flag,
        jump,
        jump_zero,
        jump_positive,
        jump_negative,
        space,
        add,
        subtract,
        multiply,
        divide,
        modulo,
        copy,
        read
    ]

    numbers = ["ZRO", "ONE", "TWO", "THR", "FUR", "FVE", "SIX", "SVN", "EGH", "NNE", "NEG"]

    numeric: list = {
        numbers[0]: "0",
        numbers[1]: "1",
        numbers[2]: "2",
        numbers[3]: "3",
        numbers[4]: "4",
        numbers[5]: "5",
        numbers[6]: "6",
        numbers[7]: "7",
        numbers[8]: "8",
        numbers[9]: "9",
        numbers[10]: "-"
    }

    def is_valid(self, data):
        if data in self.tokens:
            return True
        return data in self.numbers

    def check(self, data, token):
        return data == token

    def sequence_check(self, token: list):
        for idx in range(len(token)):
            if not self.check(data[index + idx], token[idx]):
                return False
        return True

    def read_to_endline(self):
        global index
        text = []
        while data[index] != self.endline:
            if data[index] == self.newline:
                text.append("\n")
            else:
                if data[index] == self.space:
                    text.append("")
                else:
                    text.append(data[index])
            index += 1
        return " ".join(text)

    def text_to_number(self, text: str):
        text = text.replace("\n", self.newline).split(" ")
        out = ""
        newl = False
        for number in text:
            if number == "":
                continue
            if not self.is_valid(number):
                handler.yeet("Unknown key", number)
            if number == self.newline:
                newl = True
                break
            out += self.numeric[number]
        try:
            return int(out), newl
        except ValueError:
            handler.yeet("Invalid number", out)

    def is_keyword(self, data):
        if data in self.tokens + self.numbers:
            handler.yeet("Reserved key", data=data)

        # if len(data) != 3:
        #     handler.yeet("Invalid flag length (3)", data=data)

        if data.upper() != data:
            handler.yeet("Flag / variable name must be uppercase", data=data)


class Handler:
    def yeet(self, message, data):
        print(f"ERROR: {message} | {data}")
        exit()

    def end(self, message):
        print(f"END: {message}")
        exit()


handler = Handler()
token = Token()
var = ""
buffer = ""
index = 0

flag = {}
variable = {}

# print(data)

for index in range(len(data)):
    if data[index] == token.flag:
        token.is_keyword(data[index + 1])
        flag.update({data[index + 1]: index + 1})
    
    if len(data[index]) != 3 and len(data[index]) != 0:
        handler.yeet("Invalid lenght (3)", data[index])

index = 0

"""
In twisted lines, a serpent's nest
A code so dense, it's hard to rest
Variables tangled, logic awry
A python's coil, that makes me cry

Indentations deep, a maze to roam
Functions nested, a puzzle to call home
Comments scarce, a desert dry
A code so cryptic, it makes me sigh

I search for sense, in this twisted mess
But meaning hides, in this digital dress
A python's code, that's hard to read
A riddle wrapped, in a syntax creed.

-Blackbox AI
"""

# print(data)

try:
    while 1:

        # print(data[index])
        try:
            data[index]
        except IndexError:
            handler.end("File ending")

        if token.check(data[index], token.jump):
            try:
                index = flag[data[index + 1]] + 1
            except KeyError:
                handler.yeet("Invalid jump", data=data[index + 1])

        elif token.check(data[index], token.jump_zero):
            index += 1
            try:
                var = variable[data[index + 1]]
                if not isinstance(var, tuple):
                    handler.yeet("Wrong data type", data[index + 1])
            except KeyError:
                handler.yeet("Unknown variable", data=data[index + 1])

            if var[0] == 0:
                try:
                    index = flag[data[index]] + 1
                except KeyError:
                    handler.yeet("Invalid jump", data=data[index])
            else:
                index += 2

        elif token.check(data[index], token.jump_positive):
            index += 1
            try:
                var = variable[data[index + 1]]
                if not isinstance(var, tuple):
                    handler.yeet("Wrong data type", data[index + 1])
            except KeyError:
                handler.yeet("Unknown variable", data=data[index + 1])

            if var[0] > 0:
                try:
                    index = flag[data[index]] + 1
                except KeyError:
                    handler.yeet("Invalid jump", data=data[index])
            else:
                index += 2

        elif token.check(data[index], token.jump_negative):
            index += 1
            try:
                var = variable[data[index + 1]]
                if not isinstance(var, tuple):
                    handler.yeet("Wrong data type", data[index + 1])
            except KeyError:
                handler.yeet("Unknown variable", data=data[index + 1])

            if var[0] < 0:
                try:
                    index = flag[data[index]] + 1
                except KeyError:
                    handler.yeet("Invalid jump", data=data[index])
            else:
                index += 2

        if token.check(data[index], token.flag):
            # print("assas")
            index += 2

        if not token.is_valid(data[index]):
            handler.yeet(f"Unknown Key ({index})", data=data[index])

        if token.check(data[index], token.end):
            # print(data)
            handler.end("Program done")

        if token.sequence_check([token.output, token.text]):
            # print(True)
            index += 2
            buffer = token.read_to_endline()
            print(buffer, end="")

        elif token.sequence_check([token.output, token.number]):
            # print(True)
            index += 2
            buffer = token.text_to_number(token.read_to_endline())
            print(buffer[0], "\n" * buffer[1], end="")

        elif token.sequence_check([token.output, token.newline]):
            index += 2
            print("")

        elif token.sequence_check([token.output, token.variable]):
            index += 2
            try:
                buffer = variable[data[index]]
            except KeyError:
                handler.yeet("Unknown variable", data=data[index])

            if isinstance(buffer, tuple):
                print(buffer[0], "\n" * buffer[1], end="")
            else:
                print(buffer, end="")

        if token.sequence_check([token.variable, token.text]):
            index += 2
            token.is_keyword(data[index])
            var = data[index]
            index += 1
            buffer = token.read_to_endline()
            # print({var: buffer})
            variable.update({var: buffer})

        elif token.sequence_check([token.variable, token.number]):
            index += 2
            token.is_keyword(data[index])
            var = data[index]
            index += 1
            buffer = token.text_to_number(token.read_to_endline())
            # print({var: buffer})
            variable.update({var: buffer})
        
        if token.sequence_check([token.read, token.text]):
            index += 2
            token.is_keyword(data[index])
            var = data[index]
            index += 1
            buffer = input(token.read_to_endline())
            # print({var: buffer})
            variable.update({var: buffer})
        
        elif token.sequence_check([token.read, token.number]):
            index += 2
            token.is_keyword(data[index])
            var = data[index]
            index += 1
            buffer = input(token.read_to_endline())
            # print({var: buffer})
            try:
                variable.update({var: (int(buffer), False)})
            except ValueError:
                handler.yeet("Invalid input", buffer)

        if token.check(data[index], token.add):
            index += 1
            try:
                a = variable[data[index]]
                index += 1
                b = variable[data[index]]
            except KeyError:
                handler.yeet("Unknown variable", data=data[index])

            if not (isinstance(a, tuple) and isinstance(b, tuple)):
                handler.yeet("Wrong data type", f"{data[index - 1]} & {data[index]}")

            buffer = a[0] + b[0]
            variable.update({data[index -1]: (buffer, a[1] )})

        elif token.check(data[index], token.subtract):
            index += 1
            try:
                a = variable[data[index]]
                index += 1
                b = variable[data[index]]
            except KeyError:
                handler.yeet("Unknown variable", data=data[index])

            if not (isinstance(a, tuple) and isinstance(b, tuple)):
                handler.yeet("Wrong data type", f"{data[index - 1]} & {data[index]}")

            buffer = a[0] - b[0]
            variable.update({data[index - 1]: (buffer, a[1])})
        
        elif token.check(data[index], token.divide):
            index += 1
            try:
                a = variable[data[index]]
                index += 1
                b = variable[data[index]]
            except KeyError:
                handler.yeet("Unknown variable", data=data[index])

            if not (isinstance(a, tuple) and isinstance(b, tuple)):
                handler.yeet("Wrong data type", f"{data[index - 1]} & {data[index]}")

            buffer = a[0] // b[0]
            variable.update({data[index - 1]: (buffer, a[1])})
        
        elif token.check(data[index], token.multiply):
            index += 1
            try:
                a = variable[data[index]]
                index += 1
                b = variable[data[index]]
            except KeyError:
                handler.yeet("Unknown variable", data=data[index])

            if not (isinstance(a, tuple) and isinstance(b, tuple)):
                handler.yeet("Wrong data type", f"{data[index - 1]} & {data[index]}")

            buffer = a[0] * b[0]
            variable.update({data[index - 1]: (buffer, a[1])})
        
        elif token.check(data[index], token.modulo):
            index += 1
            try:
                a = variable[data[index]]
                index += 1
                b = variable[data[index]]
            except KeyError:
                handler.yeet("Unknown variable", data=data[index])

            if not (isinstance(a, tuple) and isinstance(b, tuple)):
                handler.yeet("Wrong data type", f"{data[index - 1]} & {data[index]}")

            buffer = a[0] % b[0]
            variable.update({data[index - 1]: (buffer, a[1])})
        
        elif token.check(data[index], token.copy):
            index += 1
            try:
                a = variable[data[index]]
                index += 1
                b = variable[data[index]]
            except KeyError:
                handler.yeet("Unknown variable", data=data[index])

            if not (isinstance(a, tuple) and isinstance(b, tuple)):
                handler.yeet("Wrong data type", f"{data[index - 1]} & {data[index]}")

            variable.update({data[index - 1]: (b[0], a[1])})

        index += 1
except KeyboardInterrupt:
    # print(data)
    handler.end("Program interupt")
