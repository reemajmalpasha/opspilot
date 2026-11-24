pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { sh 'git log --oneline -1' }
    }
    stage('Test') {
      steps {
        sh '''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -r requirements.txt pytest httpx
          python -m pytest -q
        '''
      }
    }
    stage('Build image') {
      steps { sh 'docker build -t opspilot:$BUILD_NUMBER .' }
    }
    stage('Smoke test') {
      steps {
        sh '''
          docker rm -f opspilot-smoke || true
          docker run -d --name opspilot-smoke -p 8002:8000 opspilot:$BUILD_NUMBER
          sleep 5
          curl -fs localhost:8002/health
        '''
      }
    }
  }
  post {
    always { sh 'docker rm -f opspilot-smoke || true' }
    success { echo 'Pipeline succeeded' }
    failure { echo 'Pipeline failed' }
  }
}