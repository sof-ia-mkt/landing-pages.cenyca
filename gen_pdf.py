from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        pass
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.set_text_color(140, 140, 140)
        self.cell(0, 10, f'sof-IA Soluciones Educativas | sofiaeducacion.mx | Pag {self.page_no()}/2', align='C')

pdf = PDF('P', 'mm', 'Letter')
pdf.set_auto_page_break(auto=True, margin=18)
pdf.set_margins(18, 14, 18)

# Colors
navy = (26, 26, 46)
cyan = (0, 188, 212)
dark = (30, 30, 30)
gray = (100, 100, 100)
white = (255, 255, 255)
light_bg = (245, 247, 250)
green = (37, 211, 102)
orange = (255, 152, 0)

# ===== PAGE 1 =====
pdf.add_page()

# Header bar
pdf.set_fill_color(*navy)
pdf.rect(0, 0, 220, 32, 'F')
pdf.set_y(8)
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(*white)
pdf.cell(0, 8, 'ENTREGA DE PROYECTO', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(180, 210, 255)
pdf.cell(0, 6, 'Landing Pages de Captacion  |  CENYCA Universidad Tijuana', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(38)

# Resumen ejecutivo
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*navy)
pdf.cell(0, 7, 'RESUMEN EJECUTIVO', new_x='LMARGIN', new_y='NEXT')
pdf.set_draw_color(*cyan)
pdf.set_line_width(0.6)
pdf.line(18, pdf.get_y(), 80, pdf.get_y())
pdf.ln(3)

pdf.set_font('Helvetica', '', 8.5)
pdf.set_text_color(*dark)
pdf.multi_cell(0, 4.2, 'Desarrollo de 7 landing pages optimizadas para la captacion de prospectos para el ciclo Mayo 2025 de CENYCA Universidad, campus Tijuana. Cada pagina incluye diseno responsivo, formulario con validacion, integracion API y optimizacion SEO/OG.', new_x='LMARGIN', new_y='NEXT')
pdf.ln(3)

# Info row
pdf.set_fill_color(*light_bg)
pdf.set_font('Helvetica', 'B', 7.5)
pdf.set_text_color(*gray)
info_items = [
    ('Cliente', 'CENYCA Universidad'),
    ('Dominio', 'cenycauniversidad.mx'),
    ('Fecha', '02 de Abril, 2026'),
    ('Entrega por', 'sof-IA Soluciones Educativas')
]
col_w = 43.5
for label, val in info_items:
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.rect(x, y, col_w, 12, 'F')
    pdf.set_xy(x + 2, y + 1.5)
    pdf.set_font('Helvetica', '', 6.5)
    pdf.set_text_color(*gray)
    pdf.cell(col_w - 4, 4, label)
    pdf.set_xy(x + 2, y + 5.5)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_text_color(*dark)
    pdf.cell(col_w - 4, 5, val)
    pdf.set_xy(x + col_w + 1, y)
pdf.ln(16)

# Landing pages table
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*navy)
pdf.cell(0, 7, '7 LANDING PAGES ENTREGADAS', new_x='LMARGIN', new_y='NEXT')
pdf.set_draw_color(*cyan)
pdf.line(18, pdf.get_y(), 100, pdf.get_y())
pdf.ln(3)

carreras = [
    ('Ing. Mecatronica', '/ingenieria-mecatronica/'),
    ('Ing. Industrial', '/ingenieria-industrial/'),
    ('Ing. en Sistemas Computacionales', '/ingenieria-en-sistemas-computacionales/'),
    ('Ing. Electromecanica', '/ingenieria-electromecanica/'),
    ('Lic. Gastronomia', '/gastronomia/'),
    ('Lic. Criminologia y Criminalistica', '/criminologia-y-criminalistica/'),
    ('Lic. Administracion de Empresas', '/administracion-de-empresas/')
]

# Table header
pdf.set_fill_color(*navy)
pdf.set_text_color(*white)
pdf.set_font('Helvetica', 'B', 7)
pdf.cell(8, 6, '#', fill=True, align='C')
pdf.cell(70, 6, 'CARRERA', fill=True)
pdf.cell(96, 6, 'URL', fill=True)
pdf.ln()

for i, (nombre, ruta) in enumerate(carreras):
    bg = light_bg if i % 2 == 0 else white
    pdf.set_fill_color(*bg)
    pdf.set_text_color(*dark)
    pdf.set_font('Helvetica', '', 7)
    pdf.cell(8, 5.5, str(i + 1), fill=True, align='C')
    pdf.set_font('Helvetica', 'B', 7)
    pdf.cell(70, 5.5, nombre, fill=True)
    pdf.set_font('Helvetica', '', 6.5)
    pdf.set_text_color(0, 100, 180)
    pdf.cell(96, 5.5, f'cenycauniversidad.mx{ruta}', fill=True)
    pdf.ln()
    pdf.set_text_color(*dark)

pdf.ln(4)

# Alcance por landing
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*navy)
pdf.cell(0, 7, 'ALCANCE POR LANDING (10 SECCIONES)', new_x='LMARGIN', new_y='NEXT')
pdf.set_draw_color(*cyan)
pdf.line(18, pdf.get_y(), 110, pdf.get_y())
pdf.ln(3)

secciones = [
    'Hero con CTA', 'Video institucional', 'Perfil de egreso',
    'Plan de estudios interactivo', 'Beneficios CENYCA', 'Inversion y becas',
    'Galeria / Lightbox', 'Testimoniales', 'Formulario + API Novai',
    'Footer con contacto y mapa'
]
pdf.set_font('Helvetica', '', 7.5)
pdf.set_text_color(*dark)
col_w2 = 86
for i, sec in enumerate(secciones):
    col = 0 if i < 5 else 1
    if i == 5:
        pdf.set_xy(18 + col_w2 + 2, pdf.get_y() - 5 * 4.5)
    if col == 1:
        pdf.set_x(18 + col_w2 + 2)
    pdf.set_text_color(*cyan)
    pdf.cell(4, 4.5, '-')
    pdf.set_text_color(*dark)
    pdf.cell(col_w2 - 4, 4.5, f'{sec}', new_x='LMARGIN', new_y='NEXT')

pdf.ln(4)

# Metricas
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*navy)
pdf.cell(0, 7, 'METRICAS DEL DESARROLLO', new_x='LMARGIN', new_y='NEXT')
pdf.set_draw_color(*cyan)
pdf.line(18, pdf.get_y(), 95, pdf.get_y())
pdf.ln(3)

metricas = [
    ('9,965', 'lineas de codigo'),
    ('195', 'archivos de assets'),
    ('159', 'commits en Git'),
    ('70', 'secciones totales'),
    ('11', 'funciones JS/pagina'),
    ('6', 'breakpoints responsivos'),
    ('72.8 MB', 'peso total del proyecto')
]

pdf.set_font('Helvetica', '', 7)
col_w3 = 24.5
for i, (num, label) in enumerate(metricas):
    x = 18 + (i % 7) * col_w3
    y = pdf.get_y()
    pdf.set_xy(x, y)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(*cyan)
    pdf.cell(col_w3, 5, num, align='C')
    pdf.set_xy(x, y + 5)
    pdf.set_font('Helvetica', '', 5.5)
    pdf.set_text_color(*gray)
    pdf.cell(col_w3, 3.5, label, align='C')

pdf.ln(14)

# ===== PAGE 2 =====
pdf.add_page()

# Funcionalidades tecnicas
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*navy)
pdf.cell(0, 7, 'FUNCIONALIDADES TECNICAS', new_x='LMARGIN', new_y='NEXT')
pdf.set_draw_color(*cyan)
pdf.set_line_width(0.6)
pdf.line(18, pdf.get_y(), 100, pdf.get_y())
pdf.ln(3)

funcionalidades = [
    'Diseno 100% responsivo (mobile-first, 6 breakpoints)',
    'Formulario con validacion en tiempo real (telefono 10 digitos)',
    'Modal de exito animado al enviar formulario',
    'Integracion API Novai (POST con X-API-Key)',
    'Calculadora de becas interactiva por modalidad',
    'Galeria con lightbox y navegacion por teclado',
    'Lightbox de video institucional con YouTube embed',
    'Meta tags SEO y Open Graph para redes sociales',
    'Imagenes OG personalizadas (1200x630) para WhatsApp/Facebook',
    'Lazy loading de imagenes y assets optimizados'
]

pdf.set_font('Helvetica', '', 7.5)
for func in funcionalidades:
    pdf.set_text_color(*cyan)
    pdf.cell(4, 4.3, '>')
    pdf.set_text_color(*dark)
    pdf.cell(0, 4.3, func, new_x='LMARGIN', new_y='NEXT')

pdf.ln(3)

# Integracion API
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*navy)
pdf.cell(0, 7, 'INTEGRACION API NOVAI', new_x='LMARGIN', new_y='NEXT')
pdf.set_draw_color(*cyan)
pdf.line(18, pdf.get_y(), 90, pdf.get_y())
pdf.ln(3)

pdf.set_fill_color(30, 30, 46)
pdf.set_text_color(180, 230, 180)
pdf.set_font('Courier', '', 6.5)
api_block = (
    'POST  emma-sistema.up.railway.app/api/landing/prospect\n'
    'Header: X-API-Key: [proporcionada por Novai]\n'
    'Body:   { nombre, telefono, email, carrera, plantel, turno, source }\n'
    'Status: Integrado y listo. Pendiente: activar API Key real.'
)
pdf.multi_cell(0, 4, api_block, fill=True, new_x='LMARGIN', new_y='NEXT')
pdf.ln(3)

# Infraestructura
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*navy)
pdf.cell(0, 7, 'INFRAESTRUCTURA', new_x='LMARGIN', new_y='NEXT')
pdf.set_draw_color(*cyan)
pdf.line(18, pdf.get_y(), 75, pdf.get_y())
pdf.ln(3)

infra = [
    ('Hosting', 'Vercel (deploy automatico via CLI)'),
    ('Dominio', 'cenycauniversidad.mx (configurado)'),
    ('Repositorio', 'GitHub (sof-ia-mkt/landing-pages-cenyca)'),
    ('SSL', 'Certificado HTTPS activo'),
]

pdf.set_font('Helvetica', '', 7.5)
for label, val in infra:
    pdf.set_text_color(*cyan)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.cell(28, 4.5, label + ':')
    pdf.set_text_color(*dark)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.cell(0, 4.5, val, new_x='LMARGIN', new_y='NEXT')

pdf.ln(3)

# Proximos pasos
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*navy)
pdf.cell(0, 7, 'PROXIMOS PASOS', new_x='LMARGIN', new_y='NEXT')
pdf.set_draw_color(*cyan)
pdf.line(18, pdf.get_y(), 75, pdf.get_y())
pdf.ln(3)

pasos = [
    ('PENDIENTE', 'Activar API Key real de Novai (proporcionada por el cliente)', orange),
    ('PENDIENTE', 'Integrar Pixel de Meta/Facebook (ID proporcionado por el cliente)', orange),
    ('PENDIENTE', '3 landing pages adicionales a peticion del cliente', orange),
]

for estado, desc, color in pasos:
    pdf.set_fill_color(*color)
    pdf.set_text_color(*white)
    pdf.set_font('Helvetica', 'B', 5.5)
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.rect(x, y + 0.5, 18, 4, 'F')
    pdf.set_xy(x, y + 0.5)
    pdf.cell(18, 4, estado, align='C')
    pdf.set_xy(x + 20, y)
    pdf.set_text_color(*dark)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.cell(0, 5, desc, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(0.5)

pdf.ln(3)

# Estado de cuenta
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*navy)
pdf.cell(0, 7, 'ESTADO DE CUENTA', new_x='LMARGIN', new_y='NEXT')
pdf.set_draw_color(*cyan)
pdf.line(18, pdf.get_y(), 80, pdf.get_y())
pdf.ln(3)

# Table
pdf.set_fill_color(*navy)
pdf.set_text_color(*white)
pdf.set_font('Helvetica', 'B', 7)
pdf.cell(90, 6, 'CONCEPTO', fill=True)
pdf.cell(30, 6, 'MONTO', fill=True, align='C')
pdf.cell(54, 6, 'ESTADO', fill=True, align='C')
pdf.ln()

conceptos = [
    ('Primera landing page', '$5,000 MXN', ''),
    ('6 landing pages adicionales (x$4,000)', '$24,000 MXN', ''),
    ('Dominio cenycauniversidad.mx', '$800 MXN', ''),
    ('TOTAL DEL PROYECTO', '$29,800 MXN', ''),
    ('Anticipo 50%', '$14,900 MXN', 'PAGADO'),
    ('Contra entrega 50%', '$14,900 MXN', 'PENDIENTE'),
]

for i, (concepto, monto, estado) in enumerate(conceptos):
    bg = light_bg if i % 2 == 0 else white
    is_total = i == 3
    if is_total:
        pdf.set_fill_color(*navy)
        pdf.set_text_color(*white)
        pdf.set_font('Helvetica', 'B', 7.5)
    else:
        pdf.set_fill_color(*bg)
        pdf.set_text_color(*dark)
        pdf.set_font('Helvetica', '', 7)

    pdf.cell(90, 5.5, concepto, fill=True)
    pdf.set_font('Helvetica', 'B', 7 if not is_total else 7.5)
    pdf.cell(30, 5.5, monto, fill=True, align='C')

    if estado == 'PAGADO':
        pdf.set_fill_color(*bg)
        pdf.cell(20, 5.5, '', fill=True)
        pdf.set_fill_color(*green)
        pdf.set_text_color(*white)
        pdf.set_font('Helvetica', 'B', 6)
        pdf.cell(20, 5.5, ' PAGADO ', fill=True, align='C')
        pdf.set_fill_color(*bg)
        pdf.cell(14, 5.5, '', fill=True)
    elif estado == 'PENDIENTE':
        pdf.set_fill_color(*bg)
        pdf.cell(20, 5.5, '', fill=True)
        pdf.set_fill_color(*orange)
        pdf.set_text_color(*white)
        pdf.set_font('Helvetica', 'B', 6)
        pdf.cell(20, 5.5, ' PENDIENTE ', fill=True, align='C')
        pdf.set_fill_color(*bg)
        pdf.cell(14, 5.5, '', fill=True)
    else:
        pdf.set_fill_color(*bg) if not is_total else pdf.set_fill_color(*navy)
        pdf.cell(54, 5.5, '', fill=True)
    pdf.ln()

pdf.ln(5)

# Mantenimiento note
pdf.set_fill_color(240, 248, 255)
pdf.set_draw_color(*cyan)
y_note = pdf.get_y()
pdf.rect(18, y_note, 174, 10, 'DF')
pdf.set_xy(20, y_note + 1.5)
pdf.set_font('Helvetica', 'B', 7)
pdf.set_text_color(*navy)
pdf.cell(0, 3.5, 'MANTENIMIENTO MENSUAL:  $1,000 MXN/mes')
pdf.set_xy(20, y_note + 5.5)
pdf.set_font('Helvetica', '', 6.5)
pdf.set_text_color(*gray)
pdf.cell(0, 3.5, 'Incluye actualizaciones de contenido, soporte tecnico y monitoreo de uptime.')

pdf.ln(16)

# Footer signature
pdf.set_font('Helvetica', '', 7)
pdf.set_text_color(*gray)
pdf.cell(0, 4, 'Documento generado por sof-IA Soluciones Educativas  |  sofiaeducacion.mx  |  Marketing Educativo con Inteligencia', align='C')

# Save
output_path = r'C:\Users\axmlp\OneDrive\Desktop\Entrega-CENYCA-sof-IA.pdf'
pdf.output(output_path)
print(f'PDF generado exitosamente: {output_path}')
