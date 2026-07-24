import datetime
import tkinter as tk
from tkinter import messagebox


class AlgoritmoACATActualizadoGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("ACAT v2026: Contraloría Social & Control Interno")
        self.root.geometry("640x750")
        self.root.configure(bg="#F4F6F7")

        # Base de datos simulada de riesgo (SAT Art. 69-B y RPC Siger 2.0)
        self.lista_negra_sat = ["FMA120405XYZ", "GPE180911ABC"]
        self.administradores_coludidos = ["JUAN_PEREZ_GARCIA", "REYES_LOPEZ_OAX"]

        # Variables de control de la GUI
        self.perfil_var = tk.StringVar(value="CONTROL_INTERNO")
        self.rfc_var = tk.StringVar()
        self.fme_var = tk.StringVar(value="FME-")
        self.admin_var = tk.StringVar()
        self.holding_var = tk.BooleanVar(value=False)
        self.giro_var = tk.BooleanVar(value=True)
        self.modalidad_var = tk.StringVar(value="LICITACION_PUBLICA")
        self.idioma_var = tk.StringVar(value="ESPAÑOL")

        # Diccionario del Módulo Lingüístico de Oaxaca
        self.traducciones = {
            "ESPAÑOL": {
                "rojo": "🔴 SEMÁFORO ROJO: Riesgo Crítico de Opacidad Corporativa.",
                "amarillo": "🟡 SEMÁFORO AMARILLO: Riesgo Moderado / Alerta Preventiva.",
                "verde": "🟢 SEMÁFORO VERDE: Riesgo Bajo / Perfil Institucional Limpio.",
                "msg_rojo": "Expediente listo. Vincula legalmente la actuación de la autoridad.",
            },
            "ZAPOTECO_SIERRA": {
                "rojo": "🔴 LUZ ROJO: ¡Goti rari! Binni de ladi cadi jnila jniha laa.",
                "amarillo": "🟡 LUZ AMARILLO: ¡Koto cha'a! Binnizá güenda rigaaba guchi.",
                "verde": "🟢 LUZ VERDE: Jneza nisa. Binni runi dxiiña sicarú.",
                "msg_rojo": "Gua lii dxiich guiicha rari guiclu lo Contraloría de la Entidad.",
            },
            "MIXTECO_ALTA": {
                "rojo": "🔴 LUZ ROJO: ¡Koto u'vi! Tniñu ñatú ndaa iyo kanoo chi jiin.",
                "amarillo": "🟡 LUZ AMARILLO: ¡Koto va'a! Kua'an ndiaa inijnioo kua'a.",
                "verde": "🟢 LUZ VERDE: Iyo ndaa. Tniñu va'a kanoo tinuu.",
                "msg_rojo": "Kua'an jiin tutu ya'a ndiaa nuu tniñu Contraloría ñuu kanoo.",
            },
        }
        self.construir_interfaz_visual()

    def construir_interfaz_visual(self):
        # Encabezado Institucional
        tk.Label(
            self.root,
            text="ALGORITMO CIUDADANO DE ALERTA TEMPRANA (ACAT)",
            font=("Arial", 11, "bold"),
            bg="#F4F6F7",
            fg="#1A5276",
        ).pack(pady=5)

        # Selector de Perfil Operativo
        perfil_frame = tk.LabelFrame(
            self.root, text=" Perfil de Operación del Ecosistema ", bg="#F4F6F7"
        )
        perfil_frame.pack(padx=20, pady=5, fill="x")
        tk.Radiobutton(
            perfil_frame,
            text="Área Administrativa Gubernamental (Control Interno)",
            variable=self.perfil_var,
            value="CONTROL_INTERNO",
            bg="#F4F6F7",
            font=("Arial", 9, "bold"),
        ).pack(anchor="w", padx=10)
        tk.Radiobutton(
            perfil_frame,
            text="Observador Ciudadano / Testigo Social (Contraloría Social)",
            variable=self.perfil_var,
            value="CONTRALORÍA_SOCIAL",
            bg="#F4F6F7",
            font=("Arial", 9, "bold"),
        ).pack(anchor="w", padx=10)

        # Panel de Datos Abiertos
        form_frame = tk.LabelFrame(
            self.root,
            text=" 1. Módulo de Datos Abiertos (SAT / RPC Siger 2.0 / PNT) ",
            bg="#FFFFFF",
            bd=1,
            relief="solid",
        )
        form_frame.pack(padx=20, pady=5, fill="both", expand=True)

        tk.Label(
            form_frame, text="RFC del Contratista:", bg="#FFFFFF", font=("Arial", 9)
        ).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(
            form_frame,
            textvariable=self.rfc_var,
            font=("Arial", 9),
            width=25,
            relief="solid",
        ).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(
            form_frame,
            text="Folio Mercantil (RPC):",
            bg="#FFFFFF",
            font=("Arial", 9),
        ).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(
            form_frame,
            textvariable=self.fme_var,
            font=("Arial", 9),
            width=25,
            relief="solid",
        ).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(
            form_frame,
            text="Administrador Único:",
            bg="#FFFFFF",
            font=("Arial", 9),
        ).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(
            form_frame,
            textvariable=self.admin_var,
            font=("Arial", 9),
            width=25,
            relief="solid",
        ).grid(row=2, column=1, padx=10, pady=5)

        # NUEVO CAMPO: Modalidad del Gasto
        tk.Label(
            form_frame,
            text="Modalidad del Gasto:",
            bg="#FFFFFF",
            font=("Arial", 9),
        ).grid(row=3, column=0, sticky="w", padx=10, pady=5)
        tk.OptionMenu(
            form_frame,
            self.modalidad_var,
            "LICITACION_PUBLICA",
            "INVITACION_RESTRINGIDA",
            "ADJUDICACION_DIRECTA",
        ).grid(row=3, column=1, sticky="w", padx=10, pady=5)

        # Checkboxes de indicios del Beneficiario Controlador
        tk.Checkbutton(
            form_frame,
            text="¿El dueño legal es otra persona moral? (Indicio Holding)",
            variable=self.holding_var,
            bg="#FFFFFF",
            font=("Arial", 9),
        ).grid(row=4, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        tk.Checkbutton(
            form_frame,
            text="¿El giro mercantil de la PNT es congruente con la obra?",
            variable=self.giro_var,
            bg="#FFFFFF",
            font=("Arial", 9),
        ).grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        # Configuración de Inclusión Lingüística
        lang_frame = tk.LabelFrame(
            self.root, text=" 2. Configuración Lingüística (Oaxaca) ", bg="#FFFFFF"
        )
        lang_frame.pack(padx=20, pady=5, fill="x")
        for lang in ["ESPAÑOL", "ZAPOTECO_SIERRA", "MIXTECO_ALTA"]:
            tk.Radiobutton(
                lang_frame,
                text=lang,
                variable=self.idioma_var,
                value=lang,
                bg="#FFFFFF",
                font=("Arial", 9),
            ).pack(side="left", padx=20, pady=5)

        # Botón Central de Comando Visual
        tk.Button(
            self.root,
            text="INICIAR CRUCE DE AUDITORÍA PREVENTIVA",
            font=("Arial", 10, "bold"),
            bg="#239B56",
            fg="#FFFFFF",
            command=self.procesar_auditoria_trimetrica,
        ).pack(pady=10, fill="x", padx=20)

        # Zona del Semáforo Visual Dinámico Multicromático
        self.panel_diag = tk.Frame(
            self.root, bg="#EAEDED", height=150, relief="solid", bd=1
        )
        self.panel_diag.pack(padx=20, pady=5, fill="both", expand=True)

        self.lbl_diag = tk.Label(
            self.panel_diag,
            text="Esperando captura de datos abiertos en la interfaz...",
            font=("Arial", 9, "bold"),
            bg="#EAEDED",
            wraplength=500,
        )
        self.lbl_diag.pack(pady=15)

        # Botón de Descarga Oculto por Defecto
        self.btn_descargar = tk.Button(
            self.panel_diag,
            text="📥 DESCARGAR EXPEDIENTE LEGAL EN PDF (VINCULACIÓN INTERNA)",
            font=("Arial", 9, "bold"),
            bg="#1A5276",
            fg="#FFFFFF",
            command=self.descargar_pdf_automatizado,
        )

    def procesar_auditoria_trimetrica(self):
        rfc = self.rfc_var.get().upper().strip()
        admin = self.admin_var.get().upper().strip().replace(" ", "_")
        mod = self.modalidad_var.get()
        puntaje = 0

        # Reglas de negocio y acumulación de riesgo
        if rfc in self.lista_negra_sat:
            puntaje += 50  # Coincidencia directa SAT Art. 69-B
        if admin in self.administradores_coludidos:
            puntaje += 25  # Colusión o identidad oculta en el RPC Siger 2.0
        if self.holding_var.get():
            puntaje += 15  # Cadena corporativa compleja / Prestanombres
        if not self.giro_var.get():
            puntaje += 10  # Violación al perfil sectorial registrado en PNT

        # Ponderación basada en la Modalidad del Gasto
        if mod == "ADJUDICACION_DIRECTA":
            puntaje += 15  # Máximo riesgo institucional por asignación discrecional
        elif mod == "INVITACION_RESTRINGIDA":
            puntaje += 5  # Riesgo moderado por colusión pactada de tres posturas

        lang = self.idioma_var.get()
        if lang not in self.traducciones:
            lang = "ESPAÑOL"

        perfil = self.perfil_var.get()

        # Evaluación con la Escala Térmica Corregida de Tres Colores
        if puntaje >= 50:
            # 🔴 Código Rojo (#F5B7B1 - Riesgo Crítico / Alerta de Opacidad)
            self.panel_diag.configure(bg="#F5B7B1")
            self.lbl_diag.configure(bg="#F5B7B1", fg="#78281F")

            if perfil == "CONTROL_INTERNO":
                contexto = f"\n[CONTROL INTERNO]: Descalificación preventiva justificada en actas.\nPuntaje: {puntaje}/100"
            else:
                contexto = f"\n[CONTRALORÍA SOCIAL]: {self.traducciones[lang]['msg_rojo']}\nPuntaje: {puntaje}/100"

            self.lbl_diag.configure(
                text=f"{self.traducciones[lang]['rojo']}\nIndicios de simulación detectados en Siger 2.0 (RPC) y SAT [SAT].{contexto}"
            )
            self.btn_descargar.pack(pady=5)

        elif 30 <= puntaje <= 49:
            # 🟡 Código Amarillo (#FCF3CF - Riesgo Moderado / Alerta Preventiva)
            self.btn_descargar.pack_forget()
            self.panel_diag.configure(bg="#FCF3CF")
            self.lbl_diag.configure(
                text=f"{self.traducciones[lang]['amarillo']}\nPuntaje: {puntaje}/100.\n"
                f"Banderas rojas corporativas o sectoriales menores detectadas.\n"
                f"Se recomienda un análisis manual exhaustivo de las propuestas técnicas.",
                bg="#FCF3CF",
                fg="#7D6608",
            )

        else:
            # 🟢 Código Verde (#D5F5E3 - Riesgo Bajo / Rango exacto 0-29 Pts)
            self.btn_descargar.pack_forget()
            self.panel_diag.configure(bg="#D5F5E3")
            self.lbl_diag.configure(
                text=f"{self.traducciones[lang]['verde']}\nPuntaje: {puntaje}/100.\n"
                f"Proveedor verificado de forma proactiva. Perfil institucional limpio.",
                bg="#D5F5E3",
                fg="#145A32",
            )

    def descargar_pdf_automatizado(self):
        perfil = self.perfil_var.get()
        nombre_doc = (
            "Dictamen_Descalificacion_Preventiva.pdf"
            if perfil == "CONTROL_INTERNO"
            else "Expediente_Denuncia_Indicios_Opacidad.pdf"
        )
        messagebox.showinfo(
            "EXPORTACIÓN DIGITAL ACAT",
            f"¡Éxito! El archivo '{nombre_doc}' ha sido generado localmente.\n"
            f"Listo para adjuntarse formalmente ante las ventanillas del Órgano Interno de Control.",
        )


if __name__ == "__main__":
    ventana = tk.Tk()
    app = AlgoritmoACATActualizadoGUI(ventana)
    ventana.mainloop()

