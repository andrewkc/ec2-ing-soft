from service.csv_location_service import CSVLocationService
from service.api_location_service import APILocationService
from service.mock_location_service import MockLocationService
import unittest

class TestLocationService(unittest.TestCase):
    # Precondition: Los servicios CSV, API y Mock están inicializados correctamente.
    def setUp(self):
        self.csv_service = CSVLocationService()
        self.api_service = APILocationService()
        self.mock_service = MockLocationService()

    # Caso de éxito
    def test_csv_service(self):
        # Test Data: Coordenadas de Lima, Perú y Tokyo, Japan.
        city1, country1 = "Lima", "Peru"
        city2, country2 = "Tokyo", "Japan"

        # Test Steps: Calcular la distancia entre Lima y Tokyo usando el servicio CSV.
        distance = self.csv_service.calculate_distance(city1, country1, city2, country2)

        # Expected Result: Se espera que distance sea un número float.
        self.assertIsNotNone(distance)
        self.assertIsInstance(distance, float)

    # Caso de éxito
    def test_api_service(self):
        # Test Data: Coordenadas de Lima, Perú y Tokyo, Japan.
        city1, country1 = "Lima", "Peru"
        city2, country2 = "Tokyo", "Japan"

        # Test Steps: Calcular la distancia entre Lima y Tokyo usando el servicio API.
        distance = self.api_service.calculate_distance(city1, country1, city2, country2)

        # Expected Result: Se espera que distance sea un número float.
        self.assertIsNotNone(distance)
        self.assertIsInstance(distance, float)

    # Caso de éxito
    def test_mock_service(self):
        # Test Data: Coordenadas de Lima, Perú y Tokyo, Japan.
        city1, country1 = "Lima", "Peru"
        city2, country2 = "Tokyo", "Japan"

        # Test Steps: Calcular la distancia entre Lima y Tokyo usando el servicio Mock.
        distance = self.mock_service.calculate_distance(city1, country1, city2, country2)

        # Expected Result: Se espera que distance sea un número float.
        self.assertIsNotNone(distance)
        self.assertIsInstance(distance, float)

    # Una de las ciudades no existe
    def test_nonexistent_city(self):
        # Test Data: Ciudad inválida (InvalidCity) en lugar de Lima, Perú.
        city1, country1 = "InvalidCity", "Peru"
        city2, country2 = "Tokyo", "Japan"

        # Test Steps: Calcular la distancia entre ciudad inexistente e Tokyo usando el servicio CSV.
        distance = self.csv_service.calculate_distance(city1, country1, city2, country2)

        # Expected Result: Se espera que distance sea None.
        self.assertIsNone(distance)

    # Entregar la misma ciudad dos veces
    def test_same_city_twice(self):
        # Test Data: Coordenadas de Lima, Perú.
        city1, country1 = "Lima", "Peru"

        # Test Steps: Calcular la distancia entre Lima y Lima usando el servicio CSV.
        distance = self.csv_service.calculate_distance(city1, country1, city1, country1)

        # Expected Result: Se espera que distance sea 0.0.
        self.assertEqual(distance, 0.0)


class TestManualCases(unittest.TestCase):
    # Precondition: Los servicios CSV, API y Mock están inicializados correctamente.
    def setUp(self):
        self.csv_service = CSVLocationService()
        self.api_service = APILocationService()
        self.mock_service = MockLocationService()

    def test_manual_cases(self):
        """
        Test Cases:
        1. Caso de éxito.
        2. Una de las ciudades no existe.
        3. Entregar la misma ciudad dos veces.
        """

        # Caso de Éxito
        city1, country1 = "Lima", "Peru"
        city2, country2 = "Tokyo", "Japan"
        distance = self.csv_service.calculate_distance(city1, country1, city2, country2)
        
        # Expected Result: Se espera que distance sea un número float.
        self.assertIsNotNone(distance)
        self.assertIsInstance(distance, float)

        # Una de las ciudades no existe
        city1, country1 = "InvalidCity", "Peru"
        city2, country2 = "Tokyo", "Japan"
        distance = self.csv_service.calculate_distance(city1, country1, city2, country2)
        
        # Expected Result: Se espera que distance sea None.
        self.assertIsNone(distance)

        # Entregar la misma ciudad dos veces
        city1, country1 = "Lima", "Peru"
        distance = self.csv_service.calculate_distance(city1, country1, city1, country1)
        
        # Expected Result: Se espera que distance sea 0.0.
        self.assertEqual(distance, 0.0)