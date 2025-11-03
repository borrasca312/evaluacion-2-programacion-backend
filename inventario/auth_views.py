from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView


def registro_view(request):
    """Vista para registro de nuevos usuarios"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada exitosamente para {username}!')
            # Autenticar automáticamente después del registro
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('inventario:lista_solicitudes')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})


class CustomUserCreationView(CreateView):
    """Vista alternativa usando class-based view para registro"""
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('inventario:lista_solicitudes')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Cuenta creada exitosamente para {username}!')
        # Autenticar automáticamente después del registro
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return response