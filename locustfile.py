from locust import HttpUser, task, between

class HealthTrackUser(HttpUser):
    wait_time = between(1, 3)  # Espera entre 1-3 segundos entre peticiones

    @task
    def registrar_usuario(self):
        self.client.post("/registrar", json={
            "nombre": "test_user",
            "peso": 70
        })

    @task(3)  # Esta tarea se ejecutará 3 veces más que 'registrar_usuario'
    def actualizar_peso(self):
        self.client.post("/actualizar", json={
            "usuario": "test_user",
            "nuevo_peso": 68.5
        })