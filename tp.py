import tphate
import numpy
data = numpy.random.random((500, 200))
tphate_op = tphate.TPHATE()
data_tphate = tphate_op.fit_transform(data)
