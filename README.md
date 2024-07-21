# Proyecto Django de Dashboards Interactivos

Este proyecto es una aplicación web de Django que permite visualizar y analizar datos de ventas a través de dashboards interactivos. Los datos se cargan desde un archivo CSV y se presentan en diferentes tipos de gráficos, incluyendo barras, gráficos de área, indicadores y gráficos de dona. Los usuarios pueden seleccionar rangos de fechas para filtrar los datos y ver los resultados en tiempo real.

## Características

- **Dashboard 1:** Gráfico de barras con interpolación polinomial de orden 2.
- **Dashboard 2:** Gráfico de dona con interpolación polinomial de orden 3.
- **Dashboard 3:** Indicador de gauge con interpolación spline de orden 2.
- **Dashboard 4:** Gráfico de área con interpolación spline de orden 3.
- **Interactividad:** Los usuarios pueden seleccionar rangos de fechas para actualizar los gráficos dinámicamente.

## Requisitos

- Python 3.10 o superior
- Django 3.2
- pandas 1.3.5
- plotly 5.4.0
- numpy 1.21.2

## Instalación

1. Clona este repositorio:

    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crea un entorno virtual e instala las dependencias:

    ```sh
    python3.10 -m venv myenv
    source myenv/bin/activate  # En Windows usa `myenv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Realiza las migraciones de la base de datos:

    ```sh
    python manage.py migrate
    ```

4. Inicia el servidor de desarrollo:

    ```sh
    python manage.py runserver
    ```

5. Abre tu navegador y navega a `http://localhost:8000` para ver la aplicación en acción.

## Estructura del Proyecto

