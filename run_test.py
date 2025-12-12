import pytest
from datetime import datetime, timedelta, timezone
import shutil

# Zona horaria Argentina (UTC-3)
argentina = timezone(timedelta(hours=-3))
fecha_actual = datetime.now(argentina).strftime("%Y-%m-%d_%H-%M")

# Rutas
report_html = "reports/report.html"
report_html_historial = f"reports/historial_report/report_{fecha_actual}.html"

# Ejecutar pytest UNA sola vez
pytest.main(["test/", "--html", report_html, "--self-contained-html", "-v"])

# Copiar el reporte generado al historial
shutil.copy(report_html, report_html_historial)





# import pytest

# pytest.main(["test/","--html=reports/report.html","--self-contained-html","-v"])

# from datetime import datetime
# import pytest
# import os
# import shutil

# # Crear carpeta "reportes/reportes_html" si no existe
# output_dir = os.path.join("reportes", "reportes_html")
# os.makedirs(output_dir, exist_ok=True)

# # Generar nombre único con fecha y hora
# fecha_hora = datetime.now().strftime("%d-%m-%y_%H.%M.%S")
# reporte_nombre = f"report_{fecha_hora}.html"
# ruta_reporte = os.path.join(output_dir, reporte_nombre)

# # Lista de pruebas a ejecutar
# test_cases = [
#     #Para hacer prueba de api leer el readme.md
#     #"test/test_api_request.py",
#     "test/test_loginUsuarios.py",
#     "test/test_inventory.py",
#     "test/test_cart.py",
#     "test/test_cart_json.py",
#     "test/test_loginFake.py",
# ]

# # Argumentos de pytest con la nueva ruta
# pytest_args = test_cases + [
#     f"--html={ruta_reporte}",
#     "--self-contained-html",
#     "-v"
# ]

# # Ejecutar pytest
# pytest.main(pytest_args)

# # Copiar el mismo reporte a la raíz con nombre fijo
# shutil.copyfile(ruta_reporte, "report.html")
