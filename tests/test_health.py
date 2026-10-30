import importlib
import os
import unittest
from unittest.mock import patch


class HealthTest(unittest.TestCase):

    def test_health_returns_ok(self):
        environment = {
            "AWS_REGION": "us-east-1",
            "AWS_DYNAMODB_TABLE": "ToggleMasterAnalytics",
            "AWS_SQS_URL": "",
            "DYNAMODB_ENDPOINT_URL": "",
        }

        # Impede conexões reais com AWS durante o teste
        with patch.dict(os.environ, environment), patch("boto3.Session"):
            analytics = importlib.import_module("app")

        response = analytics.app.test_client().get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})


if __name__ == "__main__":
    unittest.main()
