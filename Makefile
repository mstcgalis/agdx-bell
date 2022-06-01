ui:
	pyuic6 window.ui -o window.py

clean:
	rm -rf build dist

alias:
	python3.9 setup.py py2app -A

app:
	python3.9 setup.py py2app

run:
	./dist/agdx-roadmap.live.app/Contents/MacOS/agdx-roadmap.live