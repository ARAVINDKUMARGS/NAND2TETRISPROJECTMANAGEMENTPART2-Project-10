from JackTokenizer import JackTokenizer

class CompilationEngine:
    def __init__(self, input_file, output_file):
        self.tokenizer = JackTokenizer(input_file)
        self.output = open(output_file, 'w')
        self.indent = 0
        self.compile_class()

    def write(self, text):
        self.output.write("  " * self.indent + text + "\n")

    def advance(self):
        if self.tokenizer.has_more_tokens():
            token = self.tokenizer.advance()
            return self.tokenizer.xml_token(token)
        return None

    def compile_class(self):
        self.write("<class>")
        self.indent += 1
        self.write(self.advance())  # class keyword
        self.write(self.advance())  # class name
        self.write(self.advance())  # {
        # Class body (simplified: compile classVarDec and subroutineDec)
        while self.tokenizer.has_more_tokens():
            t = self.tokenizer.tokens[self.tokenizer.current]
            if t in ("static", "field"):
                self.compile_class_var_dec()
            elif t in ("constructor", "function", "method"):
                self.compile_subroutine()
            elif t == "}":
                self.write(self.advance())
                break
        self.indent -= 1
        self.write("</class>")

    def compile_class_var_dec(self):
        self.write("<classVarDec>")
        self.indent += 1
        for _ in range(3):  # keyword, type, varName
            self.write(self.advance())
        while True:
            t = self.tokenizer.tokens[self.tokenizer.current]
            if t == ";":
                self.write(self.advance())
                break
            else:
                self.write(self.advance())
        self.indent -= 1
        self.write("</classVarDec>")

    def compile_subroutine(self):
        self.write("<subroutineDec>")
        self.indent += 1
        # keyword, type, name, '('
        for _ in range(4):
            self.write(self.advance())
        self.compile_parameter_list()
        self.write(self.advance())  # '{'
        self.compile_subroutine_body()
        self.indent -= 1
        self.write("</subroutineDec>")

    def compile_parameter_list(self):
        self.write("<parameterList>")
        self.indent += 1
        while True:
            t = self.tokenizer.tokens[self.tokenizer.current]
            if t == ")":
                break
            else:
                self.write(self.advance())
        self.indent -= 1
        self.write("</parameterList>")

    def compile_subroutine_body(self):
        self.write("<subroutineBody>")
        self.indent += 1
        while True:
            t = self.tokenizer.tokens[self.tokenizer.current]
            if t == "}":
                self.write(self.advance())
                break
            elif t == "var":
                self.compile_var_dec()
            else:
                self.compile_statements()
        self.indent -= 1
        self.write("</subroutineBody>")

    def compile_var_dec(self):
        self.write("<varDec>")
        self.indent += 1
        self.write(self.advance())  # var
        self.write(self.advance())  # type
        self.write(self.advance())  # varName
        while True:
            t = self.tokenizer.tokens[self.tokenizer.current]
            if t == ";":
                self.write(self.advance())
                break
            else:
                self.write(self.advance())
        self.indent -= 1
        self.write("</varDec>")

    def compile_statements(self):
        self.write("<statements>")
        self.indent += 1
        while True:
            if not self.tokenizer.has_more_tokens():
                break
            t = self.tokenizer.tokens[self.tokenizer.current]
            if t in ("let", "if", "while", "do", "return"):
                self.write(self.advance())
            else:
                break
        self.indent -= 1
        self.write("</statements>")
