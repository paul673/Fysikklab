from Scripts.plotting import Plot
from Scripts.funksjoner import stanErr, stanDev, avgEndSpeed

print("stanErr", stanErr())
print("stanDev", stanDev())
print("avgEndSpeed", avgEndSpeed())

p = Plot()
"""
p.x_t(save=True)
p.v_t(save=True)
p.y(save=True)
p.v(save=True)
p.f(save=True)
"""
p.tegning(save=True)




