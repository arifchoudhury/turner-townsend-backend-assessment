"""
Fifth is a new stack-based language. A stack is a data structure which can only have elements added to the top.
Fifth stores a stack of integers and supports commands to manipulate that stack. 
Operations always apply to the top of the stack.

Fifth supports the following arithmetic operators:

```
+ - * /
```

Each of these applies the operator to the two values on the top of the stack and pushes the
result to the top of the stack. If division results in a non-integer, round down.

Fifth also supports the following commands:

* `PUSH x` - push x onto the top of the stack, where x is a valid integer
* `POP` - remove the top element of the stack
* `SWAP` - swap the top two elements of the stack
* `DUP` - duplicate the top element of the stack

Write a python program which works as a fifth interpreter. Each line of input to the program should
represent a single fifth command. Output the result of each command to the terminal. Handle errors sensibly.

Example:
```
stack is []
PUSH 3
stack is [3]
PUSH 11
stack is [3, 11]
+
stack is [14]
DUP
stack is [14, 14]
PUSH 2
stack is [14, 14, 2]
*
stack is [14, 28]
SWAP
stack is [28, 14]
/
stack is [2]
+
ERROR
"""

class FifthInterpreter:
    
    def __init__(self): 
        self.stack = []
        
        self.commands = {
            "PUSH": self.push,
            "POP": self.pop,
            "SWAP": self.swap,
            "DUP": self.dup,
            "+": self.add,
            "-": self.minus,
            "*": self.multiply,
            "/": self.divide
        }
        
    def print_stack(self):
        print(f"Stack value is {self.stack}")
        
    def add(self):
        # lambda to x + y, method_ref used if required in arithmetic_operators
        self.arithmetic_operators(lambda x, y : x + y, method_ref="add")
    
    def minus(self):
        # lambda to x - y, method_ref used if required in arithmetic_operators
        self.arithmetic_operators(lambda x, y : x - y, method_ref="minus")
    
    def multiply(self):
        # lambda to x x y, method_ref used if required in arithmetic_operators
        self.arithmetic_operators(lambda x, y : x * y, method_ref="multiply")
    
    def divide(self):
        # lambda to x / y, use None to avoid zero division error, method_ref used in arithmetic_operators for better print statement
        self.arithmetic_operators(lambda x, y : x // y if y != 0 else None, method_ref="divide")
    
    def arithmetic_operators(self, operation, method_ref):
        
        if len(self.stack) < 2:
            print("Not enough elements in stack to do aritmetic operations")
            return
                
        # get the top two elements
        top_element = self.stack.pop()
        second_top_element = self.stack.pop()
        
        result = operation(second_top_element, top_element)
        
        # would only be None in the case of zero division
        if result is not None:
            self.stack.append(result)
        else:
            # check the method_ref to print a better message out, we could handle this further here
            if method_ref == "divide":
                # zero division results in None
                print("Unable to complete zero division, keeping stack the same")
            else:
                # something else went wrong so put the stack back to how it was
                print(f"Unable to complete {method_ref} operation, keeping stack the same")
            
            # put stack back to how it was
            self.stack.append(second_top_element)
            self.stack.append(top_element)
        
    def push(self, val):
        self.stack.append(val)
        
    def pop(self):
        if not self.stack:
            print("Stack is empty, cannot pop top element")
            return
        
        self.stack.pop(-1)

    def swap(self):
        if len(self.stack) < 2:
            print(f"Stack length is {len(self.stack)} so cannot do a swap of top two elements")
            return
        
        # replace top two values with eachother
        self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def dup(self):
        if not self.stack:
            print(f"Stack is empty, so cannot do a duplicate top element")
            return
        
        # duplicate last element in stack list
        top_element = self.stack[-1]
        self.stack.append(top_element)
        
    def validate_command(self, command):
                
        # break command into command value i.e PUSH 4 or SWAP
        command = command.split()
        
        if not command:
            print("Command cannot be empty")
            return None, None
    
        # case sensitive so upper
        command_name = command[0].upper()
        
        if command_name not in self.commands:
            print(f"Invalid command {command_name}")
            return None, None
        
        if command_name == "PUSH":
            if len(command) != 2:
                print("PUSH requires exactly one value in the command")
                return None, None
            try:
                value = int(command[1])  
                return command_name, value
            except ValueError:
                print("Push command requires an integer value")   
                return None, None
            
        # all other commands should have a length of 1 so no value
        if len(command) != 1:
            print(f"{command_name} requires no values but one was provided")
            return None, None
        
        return command_name, None        

    def process_command(self, command):
        
        command_name, value = self.validate_command(command)
        
        if command_name is None:
            return
        
        # value only None for PUSH command
        if value is not None:
            self.commands[command_name](value)
        else:
            # everything other command
            self.commands[command_name]()

def main():
    
    fifth_interpreter = FifthInterpreter()
    fifth_interpreter.print_stack()
    
    while True:
        try:
            command = input("command: ").strip()
            if command == "exit":
                break
            fifth_interpreter.process_command(command)
            fifth_interpreter.print_stack()
        except EOFError:
            break
        
if __name__ == "__main__":
    main()