from django.test import TestCase
from django.urls import reverse

class UsuarioAPITests(TestCase):
    def test_usuario_endpoint(self):
        # Monta a URL completa
        #url = reverse('usuarios', args=['@eduarda'])  # 'usuario_detail' deve ser o nome registrado no seu arquivo de urls.py
        
        # Faz uma requisição GET
        # response = self.client.get(url)
        response = self.client.get("/api/usuarios/@eduarda")

        
        # Validações
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta é 200 OK
        self.assertEqual(response.json(), {"id": 1, "nome": "maria eduarda","username": "@eduarda","email": "eduarda@gmail.com","senha": "2b869053f31a34090f3a8f14cbc73fb5b9cdde56604379c30a11b9b6f43203a4","foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw0nQQC1W3yDwpOFLJJTqmirx88ESUttZFLA&s"})  # Substitua pelo JSON esperado