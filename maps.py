import math

# LinearLand maps

def linearland_1(x, y, u):
  return (-5.2*x + 2.5*y + 3.2*u, -9*x - 0.8*y + 5.0*u)

def linearland_2(x, y, u):
  return (5.0*y, -0.9*y -9.0*x + 5*u)

def linearland_3(x, y, u):
  return (2.0*y - 1.2*x, -0.4*y + 3.6*x - 5*u)

def linearland_4(x, y, u):
  return (1.0*x - 0.4*y + 0.6*u, 1.8*x + 0.2*y - 5.0*u)

# NonlinearLand maps

def nonlinearland_1(x, y, u):
  return (3*y + u, -3*math.sin(8*x) - y)

def nonlinearland_2(x, y, u):
  return (2*y - 2*x + math.atan(4*x) + 2*u, 2*x - 2*y)

def nonlinearland_3(x, y, u):
  return (3*x*(0.5*x + 1.5*y) + 2.0*u, 3*(x-y) + u*u)

def nonlinearland_4(x, y, u):
  return (-(x-0.7)*(x+0.7)/0.1 + 5.0*u, -y + 2*u)

# SwitchingLand maps

def switchingland_1(x, y, u):
  x = x*10.0
  y = y*10.0
  u = u*5.0

  A00 = 0
  A01 = 1
  A10 = -0.5
  A11 = -0.5
  B0 = 0.5
  B1 = 0.8
  xp = 0
  yp = 0

  if (x > y):
    xp = A00*x + A01*y + B0*u + 3.0
    yp = A10*x + A11*y + B1*u
  else:
    xp = A00*x + A01*y + B0*u - 3.0
    yp = A10*x + A11*y + B1*u

  return (xp/3, yp/3)

def switchingland_2(x, y, u):
  A00 = 0.0
  A01 = -1.0
  A10 = -0.25
  A11 = 0.0

  xp = 0.0
  yp = 0.0

  if (x > 0):
    xp = A00*x + A01*y
    yp = A10*x + A11*y + 2*u
  else:
    xp = A00*x + A01*y
    yp = A10*x + A11*y - 2*u

  return (xp, yp)

def switchingland_3(x, y, u):
  x = x*10.0
  y = y*10.0
  u = u*5.0
  
  A00 = 0.0
  A01 = -1.0
  A10 = 1.0
  A11 = 0.0
  
  if (x < y):
    xp = A00*x + A01*y
    yp = A10*x + A11*y + 4.0 + u
  else:
    xp = A00*x + A01*y
    yp = A10*x + A11*y - 4.0 - u

  return (xp/4, yp/4)

def switchingland_4(x, y, u):
  x = x*10.0
  y = y*10.0
  u = u*5.0

  A00 = 0.7578
  A01 = -1.9796
  A10 = 1.7454
  A11 = -0.3350
  B0 = 0.1005
  B1 = -2.1600
  V0 = -0.1582
  V1 = 1.8467
  a = 1.2759
  
  if ((V0*x + V1*y) > 0):
    xp = A00*x + A01*y + a*B0*u
    yp = A10*x + A11*y + a*B1*u
  else:
    xp = A00*x + A01*y - a*B0*u
    yp = A10*x + A11*y - a*B1*u

  return (xp/6, yp/6)

# QuantizedLand maps

def quantizedland_1(x, y, u):
  x = x*10.0
  y = y*10.0
  u = u*5.0

  A00 = 0
  A01 = 1
  A10 = -0.5
  A11 = -0.5
  B0 = 0.5
  B1 = 0.8
  
  xp = A00*x + A01*y + B0*u
  yp = A10*x + A11*y + B1*u

  xp = 4.0 if xp > 0 else -4.0
  yp = 4.0 if yp > 0 else -4.0
  
  return (xp/5, yp/5)

def quantizedland_2(x, y, u):
  x = x*10.0
  y = y*10.0
  u = u*5.0

  A00 = 0.0
  A01 = -1.0
  A10 = 1.0
  A11 = 0.0
  B0 = 0.0
  B1 = 1.0
  
  xp = A00*x + A01*y + B0*u
  yp = A10*x + A11*y + B1*u
  
  if ((xp > 0.0) and (xp < 2.0)):
    xp = 2.0
  
  if ((xp < 0.0) and (xp > -2.0)):
    xp = -2.0
  
  if (xp > 2.0):
    xp = 4.0
  
  if (xp < -2.0):
    xp = -4.0

  if ((yp > 0.0) and (yp < 2.0)):
    yp = 2.0
  
  if ((yp < 0.0) and (yp > -2.0)):
    yp = -2.0
  
  if (yp > 2.0):
    yp = 4.0
  
  if (yp < -2.0):
    yp = -4.0

  return (xp/5, yp/5)

def quantizedland_3(x, y, u):
  x = x*10.0
  y = y*10.0
  u = u*5.0

  A00 = 0.0
  A01 = 1.0
  A10 = 1.0
  A11 = 0.0
  B0 = 0.0
  B1 = 2.0
  
  xp = A00*x + A01*y + B0*u
  yp = A10*x + A11*y + B1*u
  
  if ((xp > 0.0) and (xp < 2.0)):
    xp = 2.0
  
  if ((xp < 0.0) and (xp > -2.0)):
    xp = -2.0

  if (xp > 2.0):
    xp = 4.0

  if (xp < -2.0):
    xp = -4.0
  
  if ((yp > 0.0) and (yp < 2.0)):
    yp = 2.0
    
  if ((yp < 0.0) and (yp > -2.0)):
    yp = -2.0

  if (yp > 2.0):
    yp = 4.0

  if (yp < -2.0):
    yp = -4.0

  return (xp/5, yp/5)

def quantizedland_4(x, y, u):
  x = x*10.0
  y = y*10.0
  u = u*5.0

  xp = y + u
  yp = -(9.8/1.0)*math.sin(x) - 1.0*y
  
  xp = 2.0 if xp > 0 else -2.0
  yp = 2.0 if yp > 0 else -2.0

  return (xp/5, yp/5)

maps = [
  linearland_1,
  linearland_2,
  linearland_3,
  linearland_4,
  nonlinearland_1,
  nonlinearland_2,
  nonlinearland_3,
  nonlinearland_4,
  switchingland_1,
  switchingland_2,
  switchingland_3,
  switchingland_4,
  quantizedland_1,
  quantizedland_2,
  quantizedland_3,
  quantizedland_4,
]