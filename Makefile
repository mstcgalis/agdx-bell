ui:
	pyuic6 window.ui -o window.py

clean:
	rm -rf build dist

alias:
	python setup.py py2app -A

app:
	python setup.py py2app

run:
	./dist/MyApplication.app/Contents/MacOS/MyApplication