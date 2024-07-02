def parse_polynomial(line):
    tokens = list(map(int, line.split()))
    degree = tokens[0]
    coefficients = tokens[1:]
    poly = 0
    for i, coeff in enumerate(coefficients):
        if coeff == 1:
            poly |= (1 << (degree - i - 1))
    return poly, degree

def format_output(poly, degree):
    coefficients = []
    for i in range(degree - 1, -1, -1):
        coefficients.append((poly >> i) & 1)
    return f"{len(coefficients)} " + " ".join(map(str, coefficients))

def polynomial_mod_multiplication(f_poly, f_deg, g_poly, g_deg, h_poly, h_deg):
    # Polynomial multiplication
    result_poly = 0
    for i in range(f_deg):
        if (f_poly >> i) & 1:
            result_poly ^= g_poly << i

    # Polynomial modulo
    for i in range(f_deg + g_deg - 1, h_deg - 2, -1):
        if (result_poly >> i) & 1:
            result_poly ^= h_poly << (i - h_deg + 1)

    result_deg = max(h_deg - 1, 1)
    while result_deg > 1 and ((result_poly >> (result_deg - 1)) & 1) == 0:
        result_deg -= 1

    return result_poly, result_deg

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    T = int(data[0])
    index = 1
    results = []

    for _ in range(T):
        f_poly, f_deg = parse_polynomial(data[index])
        g_poly, g_deg = parse_polynomial(data[index + 1])
        h_poly, h_deg = parse_polynomial(data[index + 2])
        index += 3

        result_poly, result_deg = polynomial_mod_multiplication(f_poly, f_deg, g_poly, g_deg, h_poly, h_deg)
        results.append(format_output(result_poly, result_deg))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
