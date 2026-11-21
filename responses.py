def sample_responses(input_text):
    mensaje = str(input_text).lower()

    if any(palabra in mensaje for palabra in ("hola", "buenas", "buen dia")):
        return "¡Hola! Podés preguntarme cómo instalar Vistana, cómo usarla o qué formato tiene que tener el archivo."

    if any(palabra in mensaje for palabra in ("instal", "descarg", "requisito")):
        return (
            "Para instalar Vistana:\n"
            "1. Ejecutá el archivo Vistana-1.2-instalador.exe.\n"
            "2. Seguí los pasos del instalador (no necesita permisos de administrador).\n"
            "3. Al terminar, la vas a encontrar en el menú Inicio."
        )

    if any(palabra in mensaje for palabra in ("usa", "uso", "abrir", "funciona", "empez")):
        return (
            "Para usar Vistana:\n"
            "1. Tocá «Cargar archivo» y elegí tu Excel o CSV.\n"
            "2. Si querés, usá «Aplicar filtros» para elegir año, fechas, jurisdicción o delito.\n"
            "3. Tocá «Generar gráficos» para ver los resultados en las pestañas.\n"
            "4. Exportá el reporte con «Exportar PDF» o «Exportar Excel»."
        )

    if any(palabra in mensaje for palabra in ("archivo", "excel", "columna", "formato", "csv")):
        return (
            "El archivo puede ser .xlsx o .csv.\n"
            "Columnas obligatorias: legajo, fecha, hora, tipo_delito, jurisdiccion.\n"
            "Opcionales: delito, modalidad, estado, latitud, longitud, descripcion."
        )

    return "No entendí la pregunta. Probá con: ¿cómo instalo Vistana?, ¿cómo la uso? o ¿qué formato tiene el archivo?"
