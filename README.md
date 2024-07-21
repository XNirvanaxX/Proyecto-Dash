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

```plaintext
myproject/
├── dashboard/
│   ├── data/
│   │   └── ventas-supermercados-base-1996-evolucion-articulos-por-grupos-base-2008-mensuales.csv
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── styles.css
│   ├── templates/
│   │   └── dashboard/
│   │       ├── base.html
│   │       ├── dashboard1.html
│   │       ├── dashboard2.html
│   │       ├── dashboard3.html
│   │       ├── dashboard4.html
│   │       └── presentacion.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt

 ```
## Uso

    - Navega a `http://localhost:8000/dashboard1/` para ver el Dashboard 1.
    - Navega a `http://localhost:8000/dashboard2/` para ver el Dashboard 2.
    - Navega a `http://localhost:8000/dashboard3/` para ver el Dashboard 3.
    - Navega a `http://localhost:8000/dashboard4/` para ver el Dashboard 4.
    - Navega a `http://localhost:8000/presentacion/` para ver la página de presentación.
     

En cada dashboard, puedes seleccionar un rango de fechas y hacer clic en "Actualizar" para ver los datos filtrados y actualizados.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.



