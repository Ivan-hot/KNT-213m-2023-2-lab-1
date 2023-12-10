from django.test import TestCase
from django.urls import reverse

class URLSTestCase(TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_get_main_index(self) -> None:
        r = self.client.get(reverse('main_index'))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, "./main/index.html")

    def test_post_main_index(self) -> None:
        r = self.client.post(reverse('main_index'))
        self.assertEqual(r.status_code, 405)
    
    def test_put_main_index(self) -> None:
        r = self.client.put(reverse('main_index'))
        self.assertEqual(r.status_code, 405)
    
    def test_patch_main_index(self) -> None:
        r = self.client.patch(reverse('main_index'))
        self.assertEqual(r.status_code, 405)
    
    def test_delete_main_index(self) -> None:
        r = self.client.delete(reverse('main_index'))
        self.assertEqual(r.status_code, 405)

    def test_get_analysis_index(self) -> None:
        r = self.client.get(reverse('analysis_index'))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, "./analysis/index.html")
    
    def test_post_analysis_index(self) -> None:
        r = self.client.post(reverse('analysis_index'))
        self.assertEqual(r.status_code, 405)
    
    def test_put_analysis_index(self) -> None:
        r = self.client.put(reverse('analysis_index'))
        self.assertEqual(r.status_code, 405)
    
    def test_patch_analysis_index(self) -> None:
        r = self.client.patch(reverse('analysis_index'))
        self.assertEqual(r.status_code, 405)
    
    def test_delete_analysis_index(self) -> None:
        r = self.client.delete(reverse('analysis_index'))
        self.assertEqual(r.status_code, 405)

    def test_get_classification_index(self) -> None:
        r = self.client.get(reverse('classification_index'))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, "./classification/index.html")
    
    def test_post_classification_index(self) -> None:
        r = self.client.post(reverse('classification_index'))
        self.assertEqual(r.status_code, 405)
    
    def test_put_classification_index(self) -> None:
        r = self.client.put(reverse('classification_index'))
        self.assertEqual(r.status_code, 405)
    
    def test_patch_classification_index(self) -> None:
        r = self.client.patch(reverse('classification_index'))
        self.assertEqual(r.status_code, 405)
    
    def test_delete_classification_index(self) -> None:
        r = self.client.delete(reverse('classification_index'))
        self.assertEqual(r.status_code, 405)

    def test_post_api_timestamps(self) -> None:
        r = self.client.post(reverse('api_timestamps'), data=[], content_type='application/json')
        self.assertEqual(r.status_code, 200)
    
    def test_get_api_timestamps(self) -> None:
        r = self.client.get(reverse('api_timestamps'))
        self.assertEqual(r.status_code, 405)
    
    def test_put_api_timestamps(self) -> None:
        r = self.client.put(reverse('api_timestamps'))
        self.assertEqual(r.status_code, 405)
    
    def test_patch_api_timestamps(self) -> None:
        r = self.client.patch(reverse('api_timestamps'))
        self.assertEqual(r.status_code, 405)
    
    def test_delete_api_timestamps(self) -> None:
        r = self.client.delete(reverse('api_timestamps'))
        self.assertEqual(r.status_code, 405)