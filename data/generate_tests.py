import random, os

# Used to generate the 10 tests for the graph

ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
SIZES = [(25,30),(50,50),(75,80),(100,100),(150,150),(200,200),(300,300),(400,400),(500,500),(750,750)]

def generate_tests(seed=42):
    random.seed(seed)
    for idx, (n, m) in enumerate(SIZES, 1):
        values = {c: random.randint(1, 10) for c in ALPHABET}
        A = "".join(random.choices(ALPHABET, k=n))
        B = "".join(random.choices(ALPHABET, k=m))
        with open(os.path.join(os.path.dirname(__file__), f"test_{idx:02d}.in"), "w") as f:
            f.write(f"{len(ALPHABET)}\n")
            for c, v in values.items():
                f.write(f"{c} {v}\n")
            f.write(f"{A}\n{B}\n")

if __name__ == "__main__":
    generate_tests()
    print("Generated test_01.in through test_10.in")