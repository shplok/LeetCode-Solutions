class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        while len(expression) > 1:
            start = max(
                expression.rfind("!"),
                expression.rfind("&"),
                expression.rfind("|"),
            )
            end = expression.find(")", start)
            subExpr = expression[start : end + 1]
            result = self.evaluateSubExpr(subExpr)
            expression = expression[:start] + result + expression[end + 1 :]

        return expression == "t"

    def evaluateSubExpr(self, subExpr: str) -> str:
        # Extract the operator and the enclosed values
        op = subExpr[0]
        values = subExpr[2:-1]

        if op == "!":
            return "f" if values == "t" else "t"
        if op == "&":
            return "f" if "f" in values else "t"
        if op == "|":
            return "t" if "t" in values else "f"

        return "f"