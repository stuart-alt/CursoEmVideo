def pagina():
    import requests
    try:
        (requests.get('http://www.pudim.cm')).content[0]
    except Exception:
        print('\033[1;31mEsta página não está acessivel no momento!\033[m')
    else:
        print('\033[1;33mEsta página esta acessivel no momento!\033[m')


pagina()
