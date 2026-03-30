import os

base_dir = r"c:\Users\axmlp\OneDrive\Desktop\landing-pages-cenyca\landing-pages.cenyca"

corrections = {
    "administracion-de-empresas": [
        ("Administración</span>", "Administración de Empresas</span>"),
        ("Administración</title>", "Administración de Empresas</title>"),
        ("estudiar Administración?", "estudiar Administración de Empresas?"),
        ("egresado de Administración", "egresado de Administración de Empresas"),
    ],
    "ciencias-de-la-educacion": [
        ("Educación</span>", "Ciencias de la Educación</span>"),
        ("Educación</title>", "Ciencias de la Educación</title>"),
        ("estudiar Educación?", "estudiar Ciencias de la Educación?"),
        ("egresado de Educación", "egresado de Ciencias de la Educación")
    ],
    "contaduria-publica-y-finanzas": [
        ("Contaduría y Finanzas</span>", "Contaduría Pública y Finanzas</span>"),
        ("Contaduría y Finanzas</title>", "Contaduría Pública y Finanzas</title>"),
        ("estudiar Contaduría y Finanzas?", "estudiar Contaduría Pública y Finanzas?"),
        ("egresado de Contaduría y Finanzas", "egresado de Contaduría Pública y Finanzas")
    ],
    "criminologia-y-criminalistica": [
        ("Criminología</span>", "Criminología y Criminalística</span>"),
        ("Criminología</title>", "Criminología y Criminalística</title>"),
        ("estudiar Criminología?", "estudiar Criminología y Criminalística?"),
        ("egresado de Criminología", "egresado de Criminología y Criminalística")
    ],
    "ingenieria-en-sistemas-computacionales": [
        ("Sistemas Comput.</span>", "Sistemas Computacionales</span>"),
        ("Sistemas Comput.</title>", "Sistemas Computacionales</title>"),
        ("estudiar Sistemas Comput.?", "estudiar Sistemas Computacionales?"),
        ("egresado de Sistemas Comput.", "egresado de Sistemas Computacionales")
    ],
    "psicologia-organizacional": [
        ("Psicología Organiz.</span>", "Psicología Organizacional</span>"),
        ("Psicología Organiz.</title>", "Psicología Organizacional</title>"),
        ("estudiar Psicología Organiz.?", "estudiar Psicología Organizacional?"),
        ("egresado de Psicología Organiz.", "egresado de Psicología Organizacional")
    ]
}

for folder, rules in corrections.items():
    index_path = os.path.join(base_dir, folder, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        for old_t, new_t in rules:
            html = html.replace(old_t, new_t)
            
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Corrected {folder}")
