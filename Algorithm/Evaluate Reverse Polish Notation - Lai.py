"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Assumption

Valid operators are +, -, *, /.
Each operand may be an integer or another expression.
Examples

["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

class Solution(object):
  def evalRPN(self, tokens):
    """
    input: string[] tokens
    return: int
    """
    # write your solution here
