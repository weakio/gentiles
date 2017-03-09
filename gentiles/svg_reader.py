from __future__ import print_function
from __future__ import unicode_literals

from xml.dom import minidom


class SVGFileReader:

    def __init__(self, filename):
        self.__filename = filename
        self.__svg_shape = []
    # end __init__


    def get_shapes_id(self):
        shapes_id = []

        svg_dom = minidom.parse(self.__filename)
        svg_node = svg_dom.getElementsByTagName('svg')[0]

        # path nodes -> SVGHexagon
        for path_node in svg_node.getElementsByTagName('path'):
            shapes_id.append(path_node.getAttribute('id'))
        # end for

        # rect nodes -> SVGRectangle + SVGIsometricSquare
        for rect_node in svg_node.getElementsByTagName('rect'):
            shapes_id.append(rect_node.getAttribute('id'))
        # end for

        return shapes_id
    # end get_shapes_ids
# end SVGFileReader


if __name__ == "__main__":
    from svg_shapes import SVGHexagon, SVGRectangle, SVGIsometricSquare
    f = SVGFileReader("/tmp/all.svg")
    shapes_id = f.get_shapes_id()
    print(shapes_id)
# end if
