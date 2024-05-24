print("abc")
print(__name__)
if __name__ == "__main__":
    a = [1,2,3,4]
    b = a
    print(a,b,id(a),id(b))
    b[0] = 9
    print(a,b,id(a),id(b))
    b = []
    print(a,b,id(a),id(b))
print("euh")   