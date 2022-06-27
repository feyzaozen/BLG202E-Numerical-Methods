# Feyza Özen 150190014
import numpy
from scipy import linalg
import matplotlib.pyplot

clown_img = matplotlib.pyplot.imread("clown.bmp")
figure = matplotlib.pyplot.figure()

r = 2
i = 1

while r < 64:  #compressing given image matrix 
    u, singular, v = numpy.linalg.svd(clown_img)

    u = u[:, :r]
    v = v[:r, :]
    s = numpy.diag(singular)
    s = s[:r, :r]
    compressed = numpy.dot(numpy.dot(u, s), v)
    figure.add_subplot(3, 2, i) # using the matplotlib subplots2 for each of the pictures, with 3(nrows) and 2(ncols) as the first two arguments.


    matplotlib.pyplot.imshow(compressed, cmap="gray")

    r = r * 2 #Starts with rank r = 2 and go up by powers of 2, to r = 64.
    i = i + 1

matplotlib.pyplot.show()
figure.savefig("clowns.png")




