DESTDIR = $(HOME)
SHELL = /bin/bash
INSFLAGS = -m 0755

#############################################################################
.PHONY: all clean install pack test doc run profile
all: dist/calc/calc

dist/calc/calc: calc.py
        #pip install PyQt5 2> /dev/null || pip3 install PyQt5 2> /dev/null
    pyi-makespec calc.py
    pyinstaller calc.spec

clean:
    rm -rf ./build
    rm -rf ./dist
    rm -f calc.spec
    
pack:
    zip -r xgajdo30_xgaven08_xvalas10_xhatal01.zip *
doc:
    doxygen ../Doxyfile
run:
    python calc.py

install: dist/calc/calc
    mkdir -p $(DESTDIR)/opt
    cd dist; find calc -type f -exec install -D $(INSFLAGS) "{}" "$(DESTDIR)/opt/{}" \;
