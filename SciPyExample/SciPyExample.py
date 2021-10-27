from scipy import optimize

def Paraboloid(x):
    z = x[0]**2 + x[1]**2
    return z

bounds = [(-3, 3), (-3, 3)]

results = dict()
results['cg'] = optimize.minimize(Paraboloid, [1.0, 1.0], method="CG")  

print(results['cg'])
