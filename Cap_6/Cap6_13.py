agency = {'CCC':' Civilian Conservation Corps',
          'FCC':'Federal Communications Commission',
          'FDIC':'Federal Deposit Insurance Corporation',
          'SSB':'Social Securit Board',
          'WPA':'Work Progress Administration'}
#item a
print(agency)
print()
acc_1 = {'SEC':'Securities and Exchange Commission'}
agency.update(acc_1)
print(agency)
print()

#item b
acc_2 = {'SSB':'Social Sgurity Administration'}
agency.update(acc_2)
print(agency)
print()

#item c
agency.pop('CCC', 'WPA')
print(agency)
