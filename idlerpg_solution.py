data = [[0x957d3d19b4d2a, 0o112575172146646270],[0x2123efad3594b3, 0o411076765515312077],[0x14a976197c2915, 0o245227303137024262],[0x93dbfd1c5928f, 0o111733772161311037],[0x147f84671e56d, 0o12177410634362362],[0xf036125564a45, 0o170066044525444727],[0x723a8f0523b99, 0o71072436024435551],[0x1b05a7c82fd37a, 0o330132371013751406],[0xdd2ea5ce253cf, 0o156456513470451560],[0x962f5786b2bc8, 0o113057257032625565],[0xbb0e5e66a974a, 0o135416274632513432],[0x6c1cbf73e807b, 0o66034576717500034],[0x267abd0c92e17, 0o23172572062226746],[0x191edd987d99db, 0o310755663037314567],[0xc3018045513b0, 0o141401400425211504],[0x4810904aed9ad, 0o44020440453554572],[0x1ffa7a900063e4, 0o377647522000061605],[0x1185db7ab832fc, 0o214135557256031310],[0x208c01f7ff8f55, 0o404300076777707357],[0x1204c1acf2a0cf, 0o220114065474520133],[0x194749d970ca7, 0o14507223545606164],[0xcc26fb68a1315, 0o146046766642411303],[0x70d920ffd960, 0o3415444077754401],[0x19ded68575f483, 0o316755320535372042],[0x2f81c8def09eb, 0o27601621573604672],[0x4a21a24bfe0a7, 0o45041504457760136],[0x2091f66c71e4ad, 0o404437315434362060]]

print(type(data))
print(len(data))

for i in data:
    print(chr(i[0]-i[1]), end="")