#!python2
#coding=utf-8
# 
import cairo

WIDTH, HEIGHT = 600, 300
surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)

ctx.set_source_rgb(1, 1, 1)
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()


ctx.translate(50, 50) 
code = [0,1,0,1,1,1]

Width_per_code = 10
Height_per_code = 200

ctx.set_source_rgb(0, 0, 0)
for i, c in enumerate(code):
    xpos = Width_per_code * i
    if c:
        ctx.rectangle(xpos, 0, Width_per_code, Height_per_code)
        ctx.fill()

surface.write_to_png ("barcode1.png") # Output to PNG
