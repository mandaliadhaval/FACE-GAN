#!/usr/bin/env python
"""
Random walk face generator

Dependends on:
    * numpy 1.7
    * matplotlib
"""
import numpy
from matplotlib import pyplot
from morpher import Morpher
from importlib import reload

if __name__ == "__main__":
    # Initialize face generator
    morpher = Morpher()
    morpher.shuffle()
    # Make sure I/O doesn't hang when displaying the image
    pyplot.ion()
    
    # Build visualization window
    fig = pyplot.figure(figsize=(1, 1), dpi=300)
    im = pyplot.imshow(X=morpher.generate_face(),
                       interpolation='nearest',
                       cmap='gist_gray')
    pyplot.axis('off')
    pyplot.show()

    # Program loop
    #print ("Press CTRL+C to stop")
    #Z = morpher.get_Z()
    #print(Z)
    
    
#    while True:
#        Z = morpher.get_Z()
#        dimension = morpher.index_mapping[numpy.random.choice(29)]
#        delta = 0.5 * numpy.random.choice([-1, 1])
        # delta = numpy.random.normal(scale=0.5)
#        Z[dimension] = Z[dimension] + delta
#        morpher.set_Z(Z)
#        im.set_array(morpher.generate_face())
#        pyplot.draw()
        
        
    
    
