from __future__ import print_function
from __future__ import unicode_literals

import io

from svg_shapes import SVGShape


class SVGFileGenerator:
    def __init__(self, filename):
        self.__filename = filename
        self.__svg_shape = []
    # end __init__


    def add_shape(self, svg_shape):
        if isinstance(svg_shape, SVGShape):
            self.__svg_shape.append(svg_shape)
        # end if
    # end add_shape


    def add_shapes(self, *svg_shapes):
        for svg_shape in svg_shapes:
            self.add_shape(svg_shape)
        # end for
    # end add_shapes


    def write(self, fileobj):
        # write header
        fileobj.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
        fileobj.write('<svg\n')
        fileobj.write('xmlns="http://www.w3.org/2000/svg"\n')
        fileobj.write('xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"\n')
        fileobj.write('xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" >\n')

        # write every shape
        for shape in self.__svg_shape:
            svg = shape.generate_svg()
            fileobj.write(svg)
            fileobj.write('\n')
        # end for

        # write footer
        fileobj.write('</svg>')
    # end write


    def save(self):
        fileobj = io.open(self.__filename, mode="w", encoding="utf-8")
        self.write(fileobj)
        fileobj.close()
    # end save
# end SVGFileGenerator


if __name__ == "__main__":
    from svg_shapes import SVGHexagon, SVGRectangle, SVGIsometricSquare
    f = SVGFileGenerator('/tmp/hex.svg')
    h = SVGHexagon(10, shape_id='hex_flat_topped')
    h.stroke_width = 0.2
    f.add_shape(h)
    f.save()

    f = SVGFileGenerator('/tmp/rectangle.svg')
    r = SVGRectangle(20, 10, shape_id='square_flat_topped')
    r.stroke_width = 0.2
    f.add_shape(r)
    f.save()

    f = SVGFileGenerator('/tmp/iso_square.svg')
    s = SVGIsometricSquare(15, shape_id='isometric square')
    s.stroke_width = 0.2
    f.add_shape(s)
    f.save()


    # all in onefile
    f = SVGFileGenerator('/tmp/all.svg')
    f.add_shapes(h, r, s)
    f.save()

# end if
