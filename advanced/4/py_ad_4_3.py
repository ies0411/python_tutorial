"""
    pypi,build,package deploy
"""
# py_ad_4_3 : 완성된 패키지 임포트
from py_ad_4_3 import GifConverter as gfc

c = gfc(...)

c.convert_fig()
"""
    1. https://pypi.org 회원가입
    2. pip install django, pip install github...
    3. .gitignore
    4. LICENSE
    5. setup.py
    6. readme.md
    7. setup.cfg
    8. MENIFEST.in
    9. pip install setuptools wheel
    python -m pip install --user --upgrade setuptools wheel
    python setup.py sdist bdist_wheel

    pip install twine
    python -m twine upload dist/*


"""
