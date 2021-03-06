from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.main.models import Band
from django.urls import reverse

User = get_user_model()


class ListMyBandTest(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        user2 = User.objects.create_user(username="paquito1", password="testingpaco123", email="paco@gmail.co", first_name="Paco", last_name="Rodriguez")
        Band.objects.create(name="itacaband", web_link='https://soundcloud.com/skeewiff', playlist='https://soundcloud.com/dj-elye/sets/jazz', email="skeewiff@gmail.com", mobile="000000000", user=user1)
        Band.objects.create(name="metallica", web_link='https://soundcloud.com/tessatioarina', playlist='https://soundcloud.com/dj-elye/sets/jazz', email="metallica@gmail.com", mobile="100000000", user=user2)
        Band.objects.create(name="Maravillosa Orquesta del Alchol", web_link='https://soundcloud.com/drei-jazz', playlist='https://soundcloud.com/dj-elye/sets/jazz', email="tessatioarina@gmail.com", mobile="200000000", user=user1)
        Band.objects.create(name="Oques Grasses", web_link='https://soundcloud.com/angelo-mikha', playlist='https://soundcloud.com/dj-elye/sets/jazz',  email="angelo@gmail.com", mobile="300000000", user=user1)


    def test_bands_list(self):
        self.client.login(username='paquito', password='testingpaco123')
        response = self.client.get(reverse('mybands'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "skeewiff@gmail.com")
        self.assertNotContains(response, "metallica@gmail.com")
        self.assertContains(response, "angelo@gmail.com")
        self.assertContains(response, "tessatioarina@gmail.com")
        self.assertTemplateUsed(response, 'band/list.html')
        self.assertTemplateUsed(response, '_base.html')

