#!/bin/bash
# Local development script

# Build Docker image
docker build -t calculator-app:latest .

# Run locally for testing
docker run -d --name calculator-app -p 5000:5000 calculator-app:latest

echo "Application is running at http://localhost:5000"
echo "Health check: http://localhost:5000/health"
echo "API documentation: http://localhost:5000"

# Test the API
echo "Testing API endpoints..."
sleep 5

curl -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{"a": 5, "b": 3}'
echo ""
curl -X POST http://localhost:5000/multiply -H "Content-Type: application/json" -d '{"a": 4, "b": 6}'
echo ""

echo "To stop the container: docker stop calculator-app && docker rm calculator-app"