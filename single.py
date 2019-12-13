import py_bsvml as bv
from ctypes import *

print("SINGLE")

bsInfo = bv.BitScopeInfo()
bsCount = bv.listBitScopes(1, pointer(bsInfo))

if bsCount == 0:
    print("Couldn't find a BitScope.")
    exit()

bs = bv.openBitScope(bsInfo.port);

outroSize = 1000
introSize = 1000
totalSize = outroSize + introSize

bv.mode(bs, bv.SINGLE)
bv.enableAnalogueChannel(bs, bv.CHA)
bv.rate(bs, 1000000)
bv.traceIntro(bs, introSize)
bv.traceOutro(bs, outroSize)
bv.traceDelay(bs, 0) # ms
bv.traceTimeout(bs, bv.getMinTimeout(bs))
bv.trigType(bs, bv.COMP)
bv.trigChannelEnable(bs, bv.CHA, True)
bv.trigChannelEdge(bs, bv.CHA, bv.RISE)
bv.trigLevel(bs, 1.5) # v
bv.trigIntro(bs, 4) # samples
bv.trigOutro(bs, 4) # samples
bv.range(bs, 5.0) # v
bv.offset(bs, 1.0) # v
bv.dumpChannel(bs, bv.CHA)
bv.dumpSize(bs, totalSize)
bv.updateBitScope(bs)

bv.trace(bs)
bv.address(bs, bv.getIntroStartAddress(bs))
bv.updateBitScope(bs)

trace = (c_ubyte * totalSize)()
bv.acquire(bs, trace)

for s in trace:
    print(s)

exit()
