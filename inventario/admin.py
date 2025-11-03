from django.contrib import admin
from .models import Categoria, Solicitud, Comentario


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ("id", "nombre", "descripcion")
	search_fields = ("nombre",)


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
	list_display = (
		"id",
		"titulo",
		"categoria",
		"creador",
		"estado",
		"prioridad",
		"fecha_creacion",
		"fecha_actualizacion",
	)
	list_filter = ("estado", "prioridad", "categoria")
	search_fields = ("titulo", "descripcion")
	autocomplete_fields = ("categoria", "creador")


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
	list_display = ("id", "solicitud", "autor", "creado_en")
	search_fields = ("cuerpo",)
	autocomplete_fields = ("solicitud", "autor")
