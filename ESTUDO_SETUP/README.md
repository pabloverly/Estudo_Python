
## REQUIZITOS
pip install twine
pip install buildozer
pip install cython
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -


## BUILD ( pip install wheel)
python setup.py sdist bdist_wheel

## UPLOAD
twine upload dist/*
twine upload --skip-existing dist/* (enviar novamente)
### INSTALL
sudo python setup.py install
