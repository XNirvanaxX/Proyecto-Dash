from django.shortcuts import render, redirect
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os
from django.http import JsonResponse

def introducir_nans(df, fraccion_nan=0.1):
    """
    Introduce NaNs en un DataFrame de manera aleatoria.
    fraccion_nan: fracción de datos a convertir en NaNs.
    """
    df = df.copy()
    mascara = np.random.rand(*df.shape) < fraccion_nan
    df[mascara] = np.nan
    return df

def vista_presentacion(request):
    return render(request, 'dashboard/presentacion.html')


def vista_inicio(request):
    return redirect('dashboard1')

def vista_dashboard1(request):
    ruta_archivo_csv = os.path.join('dashboard', 'data', 'ventas-supermercados-base-1996-evolucion-articulos-por-grupos-base-2008-mensuales.csv')
    df = pd.read_csv(ruta_archivo_csv)
    df_original = df.copy()  # Guardar copia de los datos originales

    if 'fecha_inicio' in request.GET and 'fecha_fin' in request.GET:
        fecha_inicio = pd.to_datetime(request.GET['fecha_inicio'])
        fecha_fin = pd.to_datetime(request.GET['fecha_fin'])
        df = df[(pd.to_datetime(df['indice_tiempo']) >= fecha_inicio) & (pd.to_datetime(df['indice_tiempo']) <= fecha_fin)]
    else:
        fecha_inicio = df['indice_tiempo'].min()
        fecha_fin = df['indice_tiempo'].max()

    # Introducir NaNs
    df_con_nans = introducir_nans(df)

    # Interpolación polinomial de orden 2
    df_interpolado = df_con_nans.interpolate(method='polynomial', order=2)
    
    fig_interpolado = px.bar(df_interpolado, x='indice_tiempo', y='evolucion_mensual_ventas_grupos_articulos_total', title='Evolución Mensual de Ventas (Total) - Interpolación Polinomial Orden 2')
    fig_interpolado.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )

    fig_original = px.bar(df_original, x='indice_tiempo', y='evolucion_mensual_ventas_grupos_articulos_total', title='Datos Originales')
    fig_original.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )

    grafico_interpolado = fig_interpolado.to_html(full_html=False)
    grafico_original = fig_original.to_html(full_html=False)
    return render(request, 'dashboard/dashboard1.html', {
        'grafico_interpolado': grafico_interpolado,
        'grafico_original': grafico_original,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'fecha_minima': df['indice_tiempo'].min(),
        'fecha_maxima': df['indice_tiempo'].max()
    })

def vista_dashboard2(request):
    ruta_archivo_csv = os.path.join('dashboard', 'data', 'ventas-supermercados-base-1996-evolucion-articulos-por-grupos-base-2008-mensuales.csv')
    df = pd.read_csv(ruta_archivo_csv)
    df_original = df.copy()  # Guardar copia de los datos originales

    if 'fecha_inicio' in request.GET and 'fecha_fin' in request.GET:
        fecha_inicio = pd.to_datetime(request.GET['fecha_inicio'])
        fecha_fin = pd.to_datetime(request.GET['fecha_fin'])
        df = df[(pd.to_datetime(df['indice_tiempo']) >= fecha_inicio) & (pd.to_datetime(df['indice_tiempo']) <= fecha_fin)]
    else:
        fecha_inicio = df['indice_tiempo'].min()
        fecha_fin = df['indice_tiempo'].max()

    # Introducir NaNs
    df_con_nans = introducir_nans(df)

    # Interpolación de orden 3
    df_interpolado = df_con_nans.interpolate(method='polynomial', order=3)

    fig_interpolado = px.pie(df_interpolado, values='evolucion_mensual_ventas_grupos_articulosalimentos_bebidas', names='indice_tiempo', hole=0.3, title='Distribución de Ventas de Alimentos y Bebidas - Interpolación Polinomial Orden 3')
    fig_interpolado.update_traces(textinfo='percent+label')
    fig_interpolado.update_layout(
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig_original = px.pie(df_original, values='evolucion_mensual_ventas_grupos_articulosalimentos_bebidas', names='indice_tiempo', hole=0.3, title='Datos Originales')
    fig_original.update_traces(textinfo='percent+label')
    fig_original.update_layout(
        plot_bgcolor='rgba(0,0,0,0)'
    )

    grafico_interpolado = fig_interpolado.to_html(full_html=False)
    grafico_original = fig_original.to_html(full_html=False)
    return render(request, 'dashboard/dashboard2.html', {
        'grafico_interpolado': grafico_interpolado,
        'grafico_original': grafico_original,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'fecha_minima': df['indice_tiempo'].min(),
        'fecha_maxima': df['indice_tiempo'].max()
    })

def vista_dashboard3(request):
    ruta_archivo_csv = os.path.join('dashboard', 'data', 'ventas-supermercados-base-1996-evolucion-articulos-por-grupos-base-2008-mensuales.csv')
    df = pd.read_csv(ruta_archivo_csv)
    df_original = df.copy()  # Guardar copia de los datos originales

    if 'fecha_inicio' in request.GET and 'fecha_fin' in request.GET:
        fecha_inicio = pd.to_datetime(request.GET['fecha_inicio'])
        fecha_fin = pd.to_datetime(request.GET['fecha_fin'])
        df = df[(pd.to_datetime(df['indice_tiempo']) >= fecha_inicio) & (pd.to_datetime(df['indice_tiempo']) <= fecha_fin)]
    else:
        fecha_inicio = df['indice_tiempo'].min()
        fecha_fin = df['indice_tiempo'].max()

    # Introducir NaNs
    df_con_nans = introducir_nans(df)

    # Interpolación spline de orden 2
    df_interpolado = df_con_nans.interpolate(method='spline', order=2)

    fig_interpolado = go.Figure(go.Indicator(
        mode="gauge+number",
        value=df_interpolado['evol_mensual_ventas_articulosarticulos_limpieza_perfumeria'].mean(),
        title={'text': "Promedio de Ventas de Artículos de Limpieza y Perfumería - Interpolación Spline Orden 2"},
        gauge={'axis': {'range': [None, df_interpolado['evol_mensual_ventas_articulosarticulos_limpieza_perfumeria'].max()]}}
    ))
    fig_interpolado.update_layout(
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig_original = go.Figure(go.Indicator(
        mode="gauge+number",
        value=df_original['evol_mensual_ventas_articulosarticulos_limpieza_perfumeria'].mean(),
        title={'text': "Datos Originales"},
        gauge={'axis': {'range': [None, df_original['evol_mensual_ventas_articulosarticulos_limpieza_perfumeria'].max()]}}
    ))
    fig_original.update_layout(
        plot_bgcolor='rgba(0,0,0,0)'
    )

    grafico_interpolado = fig_interpolado.to_html(full_html=False)
    grafico_original = fig_original.to_html(full_html=False)
    return render(request, 'dashboard/dashboard3.html', {
        'grafico_interpolado': grafico_interpolado,
        'grafico_original': grafico_original,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'fecha_minima': df['indice_tiempo'].min(),
        'fecha_maxima': df['indice_tiempo'].max()
    })

def vista_dashboard4(request):
    ruta_archivo_csv = os.path.join('dashboard', 'data', 'ventas-supermercados-base-1996-evolucion-articulos-por-grupos-base-2008-mensuales.csv')
    df = pd.read_csv(ruta_archivo_csv)
    df_original = df.copy()  # Guardar copia de los datos originales

    if 'fecha_inicio' in request.GET and 'fecha_fin' in request.GET:
        fecha_inicio = pd.to_datetime(request.GET['fecha_inicio'])
        fecha_fin = pd.to_datetime(request.GET['fecha_fin'])
        df = df[(pd.to_datetime(df['indice_tiempo']) >= fecha_inicio) & (pd.to_datetime(df['indice_tiempo']) <= fecha_fin)]
    else:
        fecha_inicio = df['indice_tiempo'].min()
        fecha_fin = df['indice_tiempo'].max()

    # Introducir NaNs
    df_con_nans = introducir_nans(df)

    # Interpolación spline de orden 3
    df_interpolado = df_con_nans.interpolate(method='spline', order=3)

    fig_interpolado = px.area(df_interpolado, x='indice_tiempo', y='evol_mensual_ventas_articulos_indumentaria_calzado_textiles', title='Evolución Mensual de Ventas de Indumentaria, Calzado y Textiles - Interpolación Spline Orden 3')
    fig_interpolado.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )

    fig_original = px.area(df_original, x='indice_tiempo', y='evol_mensual_ventas_articulos_indumentaria_calzado_textiles', title='Datos Originales')
    fig_original.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )

    grafico_interpolado = fig_interpolado.to_html(full_html=False)
    grafico_original = fig_original.to_html(full_html=False)
    return render(request, 'dashboard/dashboard4.html', {
        'grafico_interpolado': grafico_interpolado,
        'grafico_original': grafico_original,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'fecha_minima': df['indice_tiempo'].min(),
        'fecha_maxima': df['indice_tiempo'].max()
    })

def actualizar_dashboard1(request):
    ruta_archivo_csv = os.path.join('dashboard', 'data', 'ventas-supermercados-base-1996-evolucion-articulos-por-grupos-base-2008-mensuales.csv')
    df = pd.read_csv(ruta_archivo_csv)

    fecha_inicio = pd.to_datetime(request.GET.get('fecha_inicio'))
    fecha_fin = pd.to_datetime(request.GET.get('fecha_fin'))
    df_filtrado = df[(pd.to_datetime(df['indice_tiempo']) >= fecha_inicio) & (pd.to_datetime(df['indice_tiempo']) <= fecha_fin)]

    # Introducir NaNs
    df_con_nans = introducir_nans(df_filtrado)

    # Interpolación polinomial de orden 2
    df_interpolado = df_con_nans.interpolate(method='polynomial', order=2)

    fig_interpolado = px.bar(df_interpolado, x='indice_tiempo', y='evolucion_mensual_ventas_grupos_articulos_total', title='Evolución Mensual de Ventas (Total) - Interpolación Polinomial Orden 2')
    fig_interpolado.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )

    grafico_interpolado = fig_interpolado.to_html(full_html=False)
    
    return JsonResponse({'grafico_interpolado': grafico_interpolado})

def actualizar_dashboard2(request):
    ruta_archivo_csv = os.path.join('dashboard', 'data', 'ventas-supermercados-base-1996-evolucion-articulos-por-grupos-base-2008-mensuales.csv')
    df = pd.read_csv(ruta_archivo_csv)

    fecha_inicio = pd.to_datetime(request.GET.get('fecha_inicio'))
    fecha_fin = pd.to_datetime(request.GET.get('fecha_fin'))
    df_filtrado = df[(pd.to_datetime(df['indice_tiempo']) >= fecha_inicio) & (pd.to_datetime(df['indice_tiempo']) <= fecha_fin)]

    # Introducir NaNs
    df_con_nans = introducir_nans(df_filtrado)

    # Interpolación de orden 3
    df_interpolado = df_con_nans.interpolate(method='polynomial', order=3)

    fig_interpolado = px.pie(df_interpolado, values='evolucion_mensual_ventas_grupos_articulosalimentos_bebidas', names='indice_tiempo', hole=0.3, title='Distribución de Ventas de Alimentos y Bebidas - Interpolación Polinomial Orden 3')
    fig_interpolado.update_traces(textinfo='percent+label')
    fig_interpolado.update_layout(
        plot_bgcolor='rgba(0,0,0,0)'
    )

    grafico_interpolado = fig_interpolado.to_html(full_html=False)
    
    return JsonResponse({'grafico_interpolado': grafico_interpolado})

def actualizar_dashboard3(request):
    ruta_archivo_csv = os.path.join('dashboard', 'data', 'ventas-supermercados-base-1996-evolucion-articulos-por-grupos-base-2008-mensuales.csv')
    df = pd.read_csv(ruta_archivo_csv)

    fecha_inicio = pd.to_datetime(request.GET.get('fecha_inicio'))
    fecha_fin = pd.to_datetime(request.GET.get('fecha_fin'))
    df_filtrado = df[(pd.to_datetime(df['indice_tiempo']) >= fecha_inicio) & (pd.to_datetime(df['indice_tiempo']) <= fecha_fin)]

    # Introducir NaNs
    df_con_nans = introducir_nans(df_filtrado)

    # Interpolación spline de orden 2
    df_interpolado = df_con_nans.interpolate(method='spline', order=2)

    fig_interpolado = go.Figure(go.Indicator(
        mode="gauge+number",
        value=df_interpolado['evol_mensual_ventas_articulosarticulos_limpieza_perfumeria'].mean(),
        title={'text': "Promedio de Ventas de Artículos de Limpieza y Perfumería - Interpolación Spline Orden 2"},
        gauge={'axis': {'range': [None, df_interpolado['evol_mensual_ventas_articulosarticulos_limpieza_perfumeria'].max()]}}
    ))
    fig_interpolado.update_layout(
        plot_bgcolor='rgba(0,0,0,0)'
    )

    grafico_interpolado = fig_interpolado.to_html(full_html=False)
    
    return JsonResponse({'grafico_interpolado': grafico_interpolado})


def actualizar_dashboard4(request):
    ruta_archivo_csv = os.path.join('dashboard', 'data', 'ventas-supermercados-base-1996-evolucion-articulos-por-grupos-base-2008-mensuales.csv')
    df = pd.read_csv(ruta_archivo_csv)

    fecha_inicio = pd.to_datetime(request.GET.get('fecha_inicio'))
    fecha_fin = pd.to_datetime(request.GET.get('fecha_fin'))
    df_filtrado = df[(pd.to_datetime(df['indice_tiempo']) >= fecha_inicio) & (pd.to_datetime(df['indice_tiempo']) <= fecha_fin)]

    # Introducir NaNs
    df_con_nans = introducir_nans(df_filtrado)

    # Interpolación spline de orden 3
    df_interpolado = df_con_nans.interpolate(method='spline', order=3)

    fig_interpolado = px.area(df_interpolado, x='indice_tiempo', y='evol_mensual_ventas_articulos_indumentaria_calzado_textiles', title='Evolución Mensual de Ventas de Indumentaria, Calzado y Textiles - Interpolación Spline Orden 3')
    fig_interpolado.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )

    grafico_interpolado = fig_interpolado.to_html(full_html=False)
    
    return JsonResponse({'grafico_interpolado': grafico_interpolado})

def vista_accion1(request):
    return redirect('dashboard1')

def vista_accion2(request):
    return redirect('dashboard1')

