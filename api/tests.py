from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Tower

User = get_user_model()

class TowerAPITests(TestCase):
    def setUp(self):
        # Create a test user to act as the tower owner
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Authenticate API client as this user
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Now add owner to tower data
        self.tower_data = {
            "name": "Test Tower",
            "location": "Lagos",
            "height_m": 50.5,
            "owner": self.user  # IMPORTANT: link the tower to test user
        }

        self.tower = Tower.objects.create(**self.tower_data)

    def test_list_towers(self):
        response = self.client.get("/api/towers/")
        self.assertEqual(response.status_code, 200)

    def test_create_tower(self):
        data = {
            "name": "Another Tower",
            "location": "Abuja",
            "height_m": 70.0,
            "owner": self.user.id
        }
        response = self.client.post("/api/towers/", data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_update_tower(self):
        data = {"name": "Updated Tower"}
        response = self.client.patch(f"/api/towers/{self.tower.id}/", data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_delete_tower(self):
        response = self.client.delete(f"/api/towers/{self.tower.id}/")
        self.assertEqual(response.status_code, 204)