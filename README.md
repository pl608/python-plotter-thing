# python-plotter-thing
A python console ploter for placing 2d points on a canvas.

# Instalation:
Not inculded in pip.
Download from github with git/Github Desktop/Download as zip.
If downloaded as a compressed folder extract to the directory for python modules or directly to the location for you program.
view [#Use](README.md#use)

# USE:
```python 
import plotter
foo = plotter.Plotter()
foo.setSize(10, 20)#10 wide 20 long (equivalent to a square in a console)
foo.addPiont((5, 10), marker='+')# Places a + right in the middle of the canvas
foo.Draw()
```

# OUTPUT:
```
point set: (5, 10)
1 |¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬|
2 |                    |
3 |                    |
4 |                    |
5 |         +          |
6 |                    |
7 |                    |
8 |                    |
9 |                    |
10|                    |
```
