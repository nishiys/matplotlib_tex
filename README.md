# Professional templates of Matplotlib graph

Professional graph with LaTeX rendering in Matplotlib as an alternative of gnuplot. 

## For TeX
.pdf or .svg format should be used.
.svg is easier to use on websites but as long as you want to create documants with vector images there is little difference between them.


## For Office product
Office products automatically convert vector style images to raster images.
.emf format is only acceptable.

### Online converter
Using online converter would be the best option.

### Inkscape
NOTE: On Mac there is no stable version currently (Mar. 21 2020)

- [Export Command Line Options](http://tavmjong.free.fr/INKSCAPE/MANUAL/html/CommandLine-Export.html)

```
# -M is identical to --export-emf
# inkscape --help shows further options
inkscape img.svg -M img.emf
```

### Imagemagick
- [ImageMagick \- Command\-line Tools](https://imagemagick.org/script/command-line-tools.php)

imagemagick only supports .emf on Windows.
NOTE: Old commands like "convert" are already replaced by "magick convert". These are currently just symbolic links to "magick ..." commands. 
