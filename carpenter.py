def WoodBlocks():
  n = int(input('n: '))

  #DIEMNTIONS
  x = int(input('x: '))
  y = int(input('y: '))
  z = int(input('z: '))

  m = int(input('m: '))
  p, q, r = [1]*m, [1]*m, [1]*m
  
  # GET USER CHOICE
  mDimesntions = int(input('N dimentions you wanna enter: '))
  if mDimesntions > 0:
    for i in range(mDimesntions):
      pn, qn, rn = [int(x) for x in input('Enter p, q, r').split()]
      p[i] = pn
      q[i] = qn
      r[i] = rn

  #CHECK IF IT IS POSSIBLE TO BUILD M BOX
  #DIVIDE VOLUME OF N BOX WITH M BOX VOLUME
  totalVolume = sum([p[i]*q[i]*r[i] for i in range(m)])
  possible = x*y*z*n/totalVolume

  #IF NOT POSSIBLE PRINT AND TERMINATE
  if not possible >= 1:
    return print('NOT POSSIBLE TO BUILD M BOX')

  print('POSSIBLE TO BUILD M BOX')

  # GET WASTED WOOD
  remaining = x*y*z*n - totalVolume

 
  print(remaining)

WoodBlocks()
