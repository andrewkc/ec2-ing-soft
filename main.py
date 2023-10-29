from service.csv_location_service import CSVLocationService
from service.api_location_service import APILocationService
from service.mock_location_service import MockLocationService
from tests.test_location_service import TestLocationService, TestManualCases
import unittest

if __name__ == "__main__":
    csv_service = CSVLocationService()
    api_service = APILocationService()
    mock_service = MockLocationService()

    city1, country1 = "Lima", "Peru"
    city2, country2 = "Tokyo", "Japan"

    distance_csv = csv_service.calculate_distance(city1, country1, city2, country2)
    distance_api = api_service.calculate_distance(city1, country1, city2, country2)
    distance_mock = mock_service.calculate_distance(city1, country1, city2, country2)

    print(f"Distancia (CSV): {distance_csv} km")
    print(f"Distancia (API): {distance_api} km")
    print(f"Distancia (Mock): {distance_mock} km")

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestLocationService))
    suite.addTests(loader.loadTestsFromTestCase(TestManualCases))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("Todas las pruebas pasaron.")
    else:
        print("Al menos una prueba falló.")