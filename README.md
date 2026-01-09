# Project 10 – Compiler I: Syntax Analysis

**Course:** Build a Modern Computer from First Principles (Nand2Tetris Part II)  
**Institution:** Hebrew University of Jerusalem  
**Author:** Aravind Kumar GS  
**Email:** aravindkumar06062006@gmail.com  
**License:** MIT (Educational purposes only)

---

## Overview

Project 10 focuses on building the **front-end of the Jack compiler**. The goal is to implement a **syntax analyzer** that parses Jack programs and outputs an **XML file** representing the program's grammatical structure.  

This project is divided into two stages:  

1. **Tokenizer (Stage I)** – Breaks `.jack` files into tokens and classifies them.  
2. **Parser / CompilationEngine (Stage II)** – Parses the tokenized input to generate XML showing the program structure.

---

## Objectives

- Implement a **JackTokenizer** to classify tokens:  
  - Keywords (`class`, `if`, `while`, etc.)  
  - Symbols (`{`, `}`, `(`, `)`, etc.)  
  - Identifiers (variable, function, class names)  
  - Integer constants  
  - String constants  

- Implement a **CompilationEngine** to parse tokenized input and output **XML** according to Jack grammar, including:  
  - Classes  
  - Subroutines  
  - Statements (`let`, `if`, `while`, `do`, `return`)  
  - Expressions (arithmetic, logical, array access)  

- Test outputs using the supplied **TextComparer** utility.

---

## Test Programs

| Program | Purpose |
|---------|---------|
| **Square Dance** | Tests parsing of most Jack language features except arrays. |
| **Expression-less Square Dance** | Tests parser without expressions for easier debugging. |
| **Array Test** | Tests array processing and related syntax. |

**Output Files:**

- Tokenizer: `XxxT.xml`  
- Parser: `Xxx.xml`  

Compare generated XML files with supplied reference files using **TextComparer**.

---

## Usage

1. **Run Tokenizer**:  
   - Input: `.jack` file  
   - Output: XML file `<tokens>` with each token classified  
   - Special XML handling: `<, >, ", &` → `&lt;, &gt;, &quot;, &amp;`

2. **Run Parser (CompilationEngine)**:  
   - Input: Tokenized XML file  
   - Output: XML showing the full structure of the Jack program

3. **Compare Output**:  
   - Use `TextComparer` to verify your XML against reference files

---

## Notes

- XML indentation is for readability; TextComparer ignores whitespace.  
- Stage your implementation: first handle everything except expressions, then add expressions.  
- Supplied Jack files are in:  
  - `projects/10/Square` (full Square Dance)  
  - `projects/10/ExpressionlessSquare` (expression-less)  
  - `projects/10/ArrayTest`  

---

## References

- Nand2Tetris Book – Chapter 10 (Syntax Analysis)  
- Nand2Tetris Tools – TextComparer utility

---

## License

MIT License – Educational purposes only. Do **not** distribute or claim as your own work.
