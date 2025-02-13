import cvxpy as cp
import numpy as np


num_pre = 10
freq = np.array([100, 40, 30, 10, 5])
size = np.array([1, 20, 8, 2, 4])

g = cp.Variable(5)
c = cp.Variable(5)
d = cp.Variable(5)

comp = 5

G = 10
C = 20
D = 30

t_g = 10
t_c = 100
t_d = 1000

obj = cp.Minimize(freq[0]*(g[0]*t_g + c[0]*t_c + d[0]*t_d + comp*(size[0]-g[0]-c[0]-d[0])) + 
                  freq[1]*(g[1]*t_g + c[1]*t_c + d[1]*t_d + comp*(size[1]-g[1]-c[1]-d[1])) +
                  freq[2]*(g[2]*t_g + c[2]*t_c + d[2]*t_d + comp*(size[2]-g[2]-c[2]-d[2])) + 
                  freq[3]*(g[3]*t_g + c[3]*t_c + d[3]*t_d + comp*(size[3]-g[3]-c[3]-d[3])) +
                  freq[4]*(g[4]*t_g + c[4]*t_c + d[4]*t_d + comp*(size[4]-g[4]-c[4]-d[4])))


constraints = [g[i]+c[i]+d[i]<=size[i] for i in range(5)]
constraints.append(cp.sum(g)<=G)
constraints.append(cp.sum(c)<=C)
constraints.append(cp.sum(d)<=D)
constraints.append(g>=0)
constraints.append(c>=0)
constraints.append(d>=0)


prob = cp.Problem(obj, constraints)

result = prob.solve()
print(result)
print(g.value)
print(c.value)
print(d.value)
