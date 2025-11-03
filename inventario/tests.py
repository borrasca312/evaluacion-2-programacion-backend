from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Categoria, Solicitud


class SolicitudesViewsTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username="u1", password="p@ss12345")
		self.categoria = Categoria.objects.create(nombre="Soporte", descripcion="General")

	def test_lista_requires_login(self):
		url = reverse("inventario:lista_solicitudes")
		res = self.client.get(url)
		self.assertEqual(res.status_code, 302)
		self.assertIn("/accounts/login/", res.url)

	def test_lista_ok_logged(self):
		self.client.login(username="u1", password="p@ss12345")
		url = reverse("inventario:lista_solicitudes")
		res = self.client.get(url)
		self.assertEqual(res.status_code, 200)

	def test_create_solicitud(self):
		self.client.login(username="u1", password="p@ss12345")
		url = reverse("inventario:crear_solicitud")
		data = {
			"titulo": "Problema con laptop",
			"descripcion": "La pantalla no enciende al arrancar.",
			"categoria": self.categoria.id,
			"prioridad": "med",
		}
		res = self.client.post(url, data)
		self.assertEqual(res.status_code, 302)
		self.assertEqual(Solicitud.objects.count(), 1)
		s = Solicitud.objects.first()
		self.assertEqual(s.creador, self.user)
