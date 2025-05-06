from mcp.server.fastmcp import FastMCP
from mcp.server.auth import settings
# from mcp.types import AuthRequest, AuthResponse

# class AllowAllAuthProvider(AuthServiceProvider):
#     async def verify(self, request: AuthRequest) -> AuthResponse:
#         return AuthResponse(is_authenticated=True, user_id="anonymous")
mcp = FastMCP(name="Calculator",host='0.0.0.0',port=8000) 
# mcp = FastMCP(name="Calculator",host='127.0.0.1',port=3000) 
# helper function for calculator
def calculator(a,b,operation) -> dict:

    if operation not in ("+", "-", "*", "/", "%", "//", "**"):
        print(operation)
        return {"Error": "Select a correct operation","data":None}
    else:
        if operation == "+":
            return {"data":a+b,"Error":None}
        elif operation == "-":
            return {"data":a-b,"Error":None}
        elif operation == "*":
            return {"data":a*b,"Error":None}
        elif operation == "/":
            if b != 0:
                return {"data":a/b,"Error":None}
            else:
                return {"Error": "Division by zero.","data":None}
        elif operation == "%":
            return {"data":a%b,"Error":None}
        elif operation == "//":
            if b != 0:
                return {"data":a//b,"Error":None}
            else:
                return {"Error": "Division by zero.","data":None}
        elif operation == "**":
            return {"data":a**b,"Error":None}
        
@mcp.tool(description="Get a result from a calculator. Supports +, -, *, /, %, //, **.")
def mcpCalculator(a,b,operation) -> str:
    print(a,b)
    """Get a result from calculator.
    Args:
        a: must be a number,
        b: must be a number
        operation: must valid operation ("+", "-", "*", "/", "%", "//", "**")
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Invalid number input."
    data = calculator(a,b,operation)
    if data["Error"]:
        return data["Error"]
    result = data["data"]

    return result

if __name__ == "__main__":
    print("maiin")
    mcp.run(transport="sse")