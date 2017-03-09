from __future__ import unicode_literals

from abc import ABCMeta
import math


class SVGShape(object):
    __metaclass__ = ABCMeta


    def __init__(self):
        self.__shape_id = ""
        self.__style_fill_color = 0xFFFFFF
        self.__style_fill_opacity = 1
        self.__style_stroke_color = 0x000000
        self.__style_stroke_width = 1
        self.__style_stroke_opacity = 1
        self.__style_stroke_dasharray = None
        self.__cx = 0
        self.__cy = 0
        self.__width = 0
        self.__height = 0
    # end __init__


    def generate_svg_style(self):
        str_stroke_dasharray  = ""
        if isinstance(self.__style_stroke_dasharray, tuple) and len(self.__style_stroke_dasharray) == 2:
            str_stroke_dasharray = "{:.1f},{:.1f}".format(self.__style_stroke_dasharray[0], self.__style_stroke_dasharray[1])
        else:
            str_stroke_dasharray = "none"
        # end if/else

        svg_style = 'style="'
        svg_style += "fill:#{:06X}".format(self.__style_fill_color)
        svg_style += ";"
        svg_style += "fill-opacity:{}".format(self.__style_fill_opacity)
        svg_style += ";"
        svg_style += "stroke:#{:06X}".format(self.__style_stroke_color)
        svg_style += ";"
        svg_style += "stroke-width:{}".format(self.__style_stroke_width)
        svg_style += ";"
        svg_style += "stroke-opacity:{}".format(self.__style_stroke_opacity)
        svg_style += ";"
        svg_style += "stroke-dasharray:{}".format(str_stroke_dasharray)
        svg_style += '"'

        return svg_style
    # end generate_svg_style


    def generate_svg_id(self):
        return 'id="{}"'.format(self.__shape_id)
    # end generate_svg_id


    ##########################################
    ########## METHODS TO IMPLEMENT ##########
    def generate_svg(self):
        raise NotImplementedError
    # end generate_svg
    ##########################################


    #####################################
    ########## GETTER / SETTER ##########
    @property
    def cx(self):
        return self.__cx
    # end cx


    @cx.setter
    def cx(self, value):
        self.__cx = value
    # end cx


    @property
    def cy(self):
        return self.__cy
    # end cy


    @cy.setter
    def cy(self, value):
        self.__cy = value
    # end cx


    @property
    def width(self):
        return self.__width
    # end cy


    @width.setter
    def width(self, value):
        self.__width = value
    # end width


    @property
    def height(self):
        return self.__height
    # end cy


    @height.setter
    def height(self, value):
        self.__height = value
    # end height


    @property
    def shape_id(self):
        return self.__shape_id
    # end shape_id


    @shape_id.setter
    def shape_id(self, value):
        self.__shape_id = value
    # end shape_id


    @property
    def fill_color(self):
        return self.__style_fill_color
    # end fill_color


    @fill_color.setter
    def fill_color(self, value):
        self.__style_fill_color = min(0xFFFFFF, max(0, value))
    # end fill_color


    @property
    def fill_opacity(self):
        return self.__style_fill_opacity
    # end fill_color


    @fill_opacity.setter
    def fill_opacity(self, value):
        self.__style_fill_color = min(1, max(0, value))
    # end fill_color


    @property
    def stroke_color(self):
        return self.__style_stroke_color
    # end stroke_color


    @stroke_color.setter
    def stroke_color(self, value):
        self.__style_stroke_color = min(0xFFFFFF, max(0, value))
    # end stroke_color


    @property
    def stroke_width(self):
        return self.__style_stroke_width
    # end stroke_width


    @stroke_width.setter
    def stroke_width(self, value):
        self.__style_stroke_width = max(0.0, value)
    # end stroke_width


    @property
    def stroke_opacity(self):
        return self.__style_stroke_opacity
    # end stroke_opacity


    @stroke_opacity.setter
    def stroke_opacity(self, value):
        self.__style_stroke_opacity = min(1, max(0, value))
    # end stroke_opacity


    @property
    def stroke_dasharray(self):
        return self.__style_stroke_dasharray
    # end stroke_dasharray


    @stroke_dasharray.setter
    def stroke_dasharray(self, value):
        """stroke_dasharray must be None or tuple(int, int)"""
        if isinstance(value, tuple) and len(value) == 2:
            self.__style_stroke_dasharray = value
        elif value is None:
            self.__style_stroke_dasharray = value
        else:
            self.__style_stroke_dasharray = "toto"
        # end if/elif/else
    # end stroke_dasharray
    #####################################

# end Shape


class SVGRectangle(SVGShape):
    def __init__(self, width, height, x=0, y=0, shape_id="rect"):
        super(SVGRectangle, self).__init__()
        self.shape_id = shape_id
        self.__width = width
        self.__height = height
        self.__cx = x
        self.__cy = y
    # end __init__


    def generate_svg(self):
        ident = 2
        svg  = '{ident}<rect\n'.format(ident=" "*ident)
        svg += '{ident}{style}\n'.format(ident=" "*(ident+2),
                                         style=self.generate_svg_style())
        svg += '{ident}{id}\n'.format(ident=" "*(ident*2),
                                      id=self.generate_svg_id())
        svg += '{ident}width="{w}"\n'.format(ident=" "*(ident*2),
                                     w=self.__width)
        svg += '{ident}height="{h}"\n'.format(ident=" "*(ident*2),
                                     h=self.__height)
        svg += '{ident}x="{x}"\n'.format(ident=" "*(ident*2),
                                     x=self.__cx)
        svg += '{ident}y="{y}"\n'.format(ident=" "*(ident*2),
                                     y=self.__cy)
        svg += '{ident}/>'.format(ident=" "*ident)

        return svg
    # end generate_svg
# end SVGRectangle


class SVGIsometricSquare(SVGShape):
    def __init__(self, width, x=0, y=0, shape_id="isometric_square"):
        super(SVGIsometricSquare, self).__init__()
        self.shape_id = shape_id
        self.__width = width
        self.__height = width
        self.__cx = x
        self.__cy = y
    # end __init__


    def generate_svg(self):
            ident = 2
            svg  = '{ident}<rect\n'.format(ident=" "*ident)
            svg += '{ident}{style}\n'.format(ident=" "*(ident+2),
                                             style=self.generate_svg_style())
            svg += '{ident}{id}\n'.format(ident=" "*(ident*2),
                                          id=self.generate_svg_id())
            svg += '{ident}width="{w}"\n'.format(ident=" "*(ident*2),
                                         w=self.__width)
            svg += '{ident}height="{h}"\n'.format(ident=" "*(ident*2),
                                         h=self.__height)
            svg += '{ident}x="{x}"\n'.format(ident=" "*(ident*2),
                                         x=self.__cx)
            svg += '{ident}y="{y}"\n'.format(ident=" "*(ident*2),
                                         y=self.__cy)
            svg += '{ident}transform="matrix(0.70710678,-0.70710678,0.70710678,0.70710678,0,0)"\n'.format(ident=" "*ident)
            svg += '{ident}/>'.format(ident=" "*ident)

            return svg
        # end generate_svg
# end SVGIsometricSquare


class SVGHexagon(SVGShape):
    """
    width  = 2*r
    height = sqrt(3)*r

    ########################################
    *TODO* :
        - flat_topped = False

    ########################################
    """
    def __init__(self, radius, x=0, y=0, flat_topped=True, shape_id="hexagon"):
        super(SVGHexagon, self).__init__()
        self.shape_id = shape_id
        self.__flat_topped = flat_topped
        self.__radius = radius
        self.__width = radius*2
        self.__height = math.sqrt(3) * radius
        self.__cx = x
        self.__cy = y
    # end __init__


    def generate_svg(self):
        if self.__flat_topped:
            return self.generate_svg_flat_topped()
        else:
            return ""
        # end if/else
    # end generate_svg


    def generate_svg_flat_topped(self):
        ident = 2
        svg  = '{ident}<path\n'.format(ident=" "*ident)
        svg += '{ident}{style}\n'.format(ident=" "*(ident+2),
                                         style=self.generate_svg_style())
        svg += '{ident}{id}\n'.format(ident=" "*(ident*2),
                                      id=self.generate_svg_id())
        svg += '{ident}sodipodi:type="star"\n'.format(ident=" "*(ident*2))
        svg += '{ident}sodipodi:sides="6"\n'.format(ident=" "*(ident*2))
        svg += '{ident}sodipodi:cx="{x}"\n'.format(ident=" "*(ident*2), x=self.__cx)
        svg += '{ident}sodipodi:cy="{y}"\n'.format(ident=" "*(ident*2), y=self.__cy)
        svg += '{ident}sodipodi:r1="{r1}"\n'.format(ident=" "*(ident*2), r1=self.__width*0.5)
        svg += '{ident}sodipodi:r2="{r2}"\n'.format(ident=" "*(ident*2), r2=self.__height*0.5)
        svg += '{ident}sodipodi:arg1="1.0471976"\n'.format(ident=" "*(ident*2))
        svg += '{ident}sodipodi:arg2="1.5707963"\n'.format(ident=" "*(ident*2))
        svg += '{ident}d="m 0,0 0,0 0,0 0,0 0,0 0,0 z"\n'.format(ident=" "*(ident*2))
        svg += '{ident}/>'.format(ident=" "*ident)

        return svg
    # end generate_svg_flat_topped

# end SVGHexagon
