from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Solicitud, Categoria
from .forms import SolicitudForm, ComentarioForm


@login_required
def editar_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)

    # Solo el creador puede editar
    if solicitud.creador != request.user:
        messages.error(request, "No tienes permiso para editar esta solicitud.")
        return redirect('inventario:detalle_solicitud', pk=pk)

    if request.method == 'POST':
        form = SolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            messages.success(request, "Solicitud actualizada correctamente.")
            return redirect('inventario:detalle_solicitud', pk=pk)
    else:
        form = SolicitudForm(instance=solicitud)

    return render(request, 'inventario/solicitud_form.html', {'form': form, 'editar': True})


@login_required
def lista_solicitudes(request):
    solicitudes = Solicitud.objects.all().order_by('-fecha_creacion')
    q = request.GET.get('q')
    estado = request.GET.get('estado')
    categoria = request.GET.get('categoria')

    if q:
        solicitudes = solicitudes.filter(Q(titulo__icontains=q) | Q(descripcion__icontains=q))
    if estado:
        solicitudes = solicitudes.filter(estado=estado)
    if categoria:
        solicitudes = solicitudes.filter(categoria__id=categoria)

    categorias = Categoria.objects.all()
    return render(request, 'inventario/lista_solicitudes.html', {
        'solicitudes': solicitudes,
        'categorias': categorias
    })
@login_required
def cerrar_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)

    # Solo el creador puede cerrar
    if solicitud.creador != request.user:
        messages.error(request, "No tienes permiso para cerrar esta solicitud.")
        return redirect('inventario:detalle_solicitud', pk=pk)

    solicitud.estado = 'cerrada'
    solicitud.save()
    messages.success(request, "Solicitud cerrada correctamente.")
    return redirect('inventario:detalle_solicitud', pk=pk)

@login_required
def eliminar_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)

    # Solo el creador puede eliminar
    if solicitud.creador != request.user:
        messages.error(request, "No tienes permiso para eliminar esta solicitud.")
        return redirect('inventario:detalle_solicitud', pk=pk)

    if request.method == 'POST':
        titulo = solicitud.titulo
        solicitud.delete()
        messages.success(request, f"Solicitud '{titulo}' eliminada correctamente.")
        return redirect('inventario:lista_solicitudes')
    
    return render(request, 'inventario/confirmar_eliminacion.html', {'solicitud': solicitud})

@login_required
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.creador = request.user
            solicitud.save()
            messages.success(request, "Solicitud creada correctamente.")
            return redirect('inventario:lista_solicitudes')
    else:
        form = SolicitudForm()
    return render(request, 'inventario/solicitud_form.html', {'form': form})

@login_required
def detalle_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    comentarios = solicitud.comentarios.all()
    if request.method == 'POST':
        c_form = ComentarioForm(request.POST)
        if c_form.is_valid():
            comentario = c_form.save(commit=False)
            comentario.solicitud = solicitud
            comentario.autor = request.user
            comentario.save()
            return redirect('inventario:detalle_solicitud', pk=pk)
    else:
        c_form = ComentarioForm()
    return render(request, 'inventario/detalle_solicitud.html', {
        'solicitud': solicitud,
        'comentarios': comentarios,
        'form': c_form
    })
