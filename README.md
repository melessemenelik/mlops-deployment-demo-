name: CI/CD Pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest

    steps:
    # Checkout repo
    - name: Checkout code
      uses: actions/checkout@v3

    # Set up Python
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    # Install dependencies
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    # Run tests
    - name: Run tests
      run: |
        pytest --maxfail=1 --disable-warnings -q

    # Build Docker image
    - name: Build Docker image
      run: |
        docker build -t mlops-demo:latest .

    # Push Docker image to GitHub Container Registry
    - name: Push Docker image
      uses: docker/login-action@v2
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    - run: |
        docker tag mlops-demo:latest ghcr.io/${{ github.repository }}/mlops-demo:latest
        docker push ghcr.io/${{ github.repository }}/mlops-demo:latest

    # Deploy to AWS SageMaker (placeholder step)
    - name: Deploy to SageMaker
      run: |
        echo "Deploying model to AWS SageMaker..."
        # Add boto3 deployment script here
