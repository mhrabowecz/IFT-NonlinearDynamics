import numpy as np

""" This code classify all possible behaviors of a 2D linear system."""

def classify_system(a, b, c, d):

    det = a*d - b*c
    tr = a + d
    delta = tr**2 - 4*det

    if det == 0:
        return 'pathological case'

    if delta < 0:
        if tr == 0:
            return 'center'
        else:
            if tr < 0:
                return 'stable spiral'
            else:
                return 'unstable spiral'

    if delta == 0:
        if b == c == 0:
            return 'star node'
        else:
            return 'degenerate node'

    if delta > 0:
        if det > 0:
            if tr > 0:
                return 'unstable node'
            else:
                return 'stable node'
        else:
            return 'saddle-node'

sample = []

N = 2000000  # Number of random matrices
mean = 1   # Mean value of the normal distribution
std = 2   # Standard deviation of the normal distribution

# Compute the relative frequencies of each case

for n in range(N):

    # Uniform distribution:
    #a = np.random.uniform(-1, 1)
    #b = np.random.uniform(-1, 1)
    #c = np.random.uniform(-1, 1)
    #d = np.random.uniform(-1, 1)

    # Normal distribution:
    a = np.random.normal(mean, std)
    b = np.random.normal(mean, std)
    c = np.random.normal(mean, std)
    d = np.random.normal(mean, std)

    sample.append(classify_system(a, b, c, d))

print(f"Pathological cases: {round((sample.count('pathological case')/N) * 100, 2)}%")
print(f"Center: {round((sample.count('center')/N )* 100, 2)}%")
print(f"Stable spiral : {round((sample.count('stable spiral')/N) *100, 2)}%")
print(f"Unstable spiral: {round((sample.count('unstable spiral')/N) * 100, 2)}%")
print(f"Stable node: {round((sample.count('stable node')/N)*100, 2)}%")
print(f"Unstable node: {round((sample.count('unstable node')/N)*100, 2)}%")
print(f"Degenerate node: {round((sample.count('degenerate node')/N)*100, 2)}%")
print(f"Star node: {round((sample.count('star node')/N)*100, 2)}%")
print(f"Saddle-node: {round((sample.count('saddle-node')/N)*100, 2)}%")

