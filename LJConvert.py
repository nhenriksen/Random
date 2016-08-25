import sys
### Written by Niel Henriksen.

Vals = {}

for i,arg in enumerate(sys.argv):
  if arg == '-rmin':
    Vals['rmin'] = float(sys.argv[i+1])
  if arg == '-sigma':
    Vals['sigma'] = float(sys.argv[i+1])
  if arg == '-epsilon':
    Vals['epsilon'] = float(sys.argv[i+1])
  if arg == '-A':
    Vals['A'] = float(sys.argv[i+1])
  if arg in ['-B','-C']:
    Vals['B'] = float(sys.argv[i+1])


if 'rmin' in Vals and not 'sigma' in Vals:
  Vals['sigma'] = Vals['rmin']/(2.0**(1.0/6.0))
if 'sigma' in Vals and not 'rmin' in Vals:
  Vals['rmin'] = Vals['sigma']*(2.0**(1.0/6.0))
if 'sigma' in Vals and 'epsilon' in Vals and (not 'A' in Vals or not 'B' in Vals):
  Vals['A'] = 4.0*Vals['epsilon']*(Vals['sigma']**12.0)
  Vals['B'] = 4.0*Vals['epsilon']*(Vals['sigma']**6.0)
if 'A' in Vals and 'B' in Vals and (not 'rmin' in Vals or not 'sigma' in Vals or not 'epsilon' in Vals):
  Vals['sigma'] = (Vals['A']/Vals['B'])**(1.0/6.0)
  Vals['rmin'] = Vals['sigma']*(2.0**(1.0/6.0))
  Vals['epsilon'] = (Vals['B']**2.0)/(4.0*Vals['A'])

for key in "rmin sigma epsilon A B".split():
  print "%8s= %15.7f" % (key,Vals[key])
