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
	rm -rf calc.spec
	rm -rf html/
	rm -rf latex/
pack:
	zip -r xgajdo30_xgaven08_xvalas10_xhatal01.zip *
doc:
	doxygen Doxyfile
run:
	python src/calc.py
test:
	pip3 install pytest 2>/dev/null || pip install pytest 2>/dev/null
	python -m pytest src/tests.py        
install: dist/calc/calc
	mkdir -p $(DESTDIR)/opt
	cd dist; find calc -type f -exec install -D $(INSFLAGS) "{}" "$(DESTDIR)/opt/{}" \;
