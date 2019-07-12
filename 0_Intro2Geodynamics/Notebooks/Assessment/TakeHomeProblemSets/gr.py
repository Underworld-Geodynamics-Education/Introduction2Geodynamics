from numpy import exp

# This is quite complicated because it includes a layer which (I think)
# extends from the surface down to b*L with viscosity v * eta.
# We don't need this so set v = 1.

## Adam B.

def analytic_growthrate(K,b=1.,v=1.):
    rf = (-16*K**3*b**3*v**2*exp(2*K*(2*b + 1)) + 32*K**3*b**3*v*exp(2*K*(2*b + 1)) - 16*K**3*b**3*exp(2*K*(2*b + 1)) + 32*K**3*b**2*v**2*exp(2*K*(2*b + 1)) - 64*K**3*b**2*v*exp(2*K*(2*b + 1)) + 32*K**3*b**2*exp(2*K*(2*b + 1)) - 16*K**3*b*v**2*exp(2*K*(2*b + 1)) + 32*K**3*b*v*exp(2*K*(2*b + 1)) - 16*K**3*b*exp(2*K*(2*b + 1)) - 4*K**2*b**2*v**2*exp(2*K*(b + 1)) + 4*K**2*b**2*v**2*exp(2*K*(3*b + 1)) + 4*K**2*b**2*exp(2*K*(b + 1)) - 4*K**2*b**2*exp(2*K*(3*b + 1)) + 8*K**2*b*v**2*exp(2*K*(b + 1)) - 8*K**2*b*v**2*exp(2*K*(3*b + 1)) - 8*K**2*b*exp(2*K*(b + 1)) + 8*K**2*b*exp(2*K*(3*b + 1)) - 4*K**2*v**2*exp(2*K*(b + 1)) + 4*K**2*v**2*exp(2*K*(3*b + 1)) + 4*K**2*exp(2*K*(b + 1)) - 4*K**2*exp(2*K*(3*b + 1)) - 4*K*b*v**2*exp(6*K*b) - 4*K*b*v**2*exp(2*K*(b + 2)) - 8*K*b*v**2*exp(2*K*(2*b + 1)) + 16*K*b*v*exp(2*K*(2*b + 1)) + 4*K*b*exp(6*K*b) + 4*K*b*exp(2*K*(b + 2)) - 8*K*b*exp(2*K*(2*b + 1)) - 16*K*v*exp(2*K*(2*b + 1)) - v**2*exp(4*K) + v**2*exp(8*K*b) - v**2*exp(4*K*b) + v**2*exp(4*K*(b + 1)) - 2*v**2*exp(2*K*(b + 1)) + 2*v**2*exp(2*K*(3*b + 1)) + 2*v*exp(4*K) - 2*v*exp(8*K*b) - 2*v*exp(4*K*b) + 2*v*exp(4*K*(b + 1)) - exp(4*K) + exp(8*K*b) - exp(4*K*b) + exp(4*K*(b + 1)) + 2*exp(2*K*(b + 1)) - 2*exp(2*K*(3*b + 1)))/(2*K*(16*K**4*b**4*v**2*exp(2*K*(2*b + 1)) - 32*K**4*b**4*v*exp(2*K*(2*b + 1)) + 16*K**4*b**4*exp(2*K*(2*b + 1)) - 32*K**4*b**3*v**2*exp(2*K*(2*b + 1)) + 64*K**4*b**3*v*exp(2*K*(2*b + 1)) - 32*K**4*b**3*exp(2*K*(2*b + 1)) + 16*K**4*b**2*v**2*exp(2*K*(2*b + 1)) - 32*K**4*b**2*v*exp(2*K*(2*b + 1)) + 16*K**4*b**2*exp(2*K*(2*b + 1)) + 4*K**2*b**2*v**2*exp(6*K*b) + 4*K**2*b**2*v**2*exp(2*K*(b + 1)) + 4*K**2*b**2*v**2*exp(2*K*(b + 2)) + 16*K**2*b**2*v**2*exp(2*K*(2*b + 1)) + 4*K**2*b**2*v**2*exp(2*K*(3*b + 1)) - 32*K**2*b**2*v*exp(2*K*(2*b + 1)) - 4*K**2*b**2*exp(6*K*b) - 4*K**2*b**2*exp(2*K*(b + 1)) - 4*K**2*b**2*exp(2*K*(b + 2)) + 16*K**2*b**2*exp(2*K*(2*b + 1)) - 4*K**2*b**2*exp(2*K*(3*b + 1)) - 8*K**2*b*v**2*exp(2*K*(b + 1)) - 16*K**2*b*v**2*exp(2*K*(2*b + 1)) - 8*K**2*b*v**2*exp(2*K*(3*b + 1)) + 32*K**2*b*v*exp(2*K*(2*b + 1)) + 8*K**2*b*exp(2*K*(b + 1)) - 16*K**2*b*exp(2*K*(2*b + 1)) + 8*K**2*b*exp(2*K*(3*b + 1)) + 4*K**2*v**2*exp(2*K*(b + 1)) + 8*K**2*v**2*exp(2*K*(2*b + 1)) + 4*K**2*v**2*exp(2*K*(3*b + 1)) - 4*K**2*exp(2*K*(b + 1)) + 8*K**2*exp(2*K*(2*b + 1)) - 4*K**2*exp(2*K*(3*b + 1)) + v**2*exp(4*K) + v**2*exp(8*K*b) + 2*v**2*exp(6*K*b) + v**2*exp(4*K*b) + v**2*exp(4*K*(b + 1)) + 2*v**2*exp(2*K*(b + 1)) + 2*v**2*exp(2*K*(b + 2)) + 4*v**2*exp(2*K*(2*b + 1)) + 2*v**2*exp(2*K*(3*b + 1)) - 2*v*exp(4*K) - 2*v*exp(8*K*b) + 2*v*exp(4*K*b) + 2*v*exp(4*K*(b + 1)) + exp(4*K) + exp(8*K*b) - 2*exp(6*K*b) + exp(4*K*b) + exp(4*K*(b + 1)) - 2*exp(2*K*(b + 1)) - 2*exp(2*K*(b + 2)) + 4*exp(2*K*(2*b + 1)) - 2*exp(2*K*(3*b + 1))))



    return rf