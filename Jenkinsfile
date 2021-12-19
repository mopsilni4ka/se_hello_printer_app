pipeline {
    agent any
    stages {
        stage('Deps') {
            steps {
	            sh 'make deps'
        	}
        }
        stage('Linter') {
            steps {
	            sh 'make lint'
        	}
        }
        stage('Test') {
            steps {
	            sh 'make test'
              sh 'make test_xunit || true'
              xunit thresholds: [
                  failed(failureThreshold: '1'),
                  skipped(failureThreshold: '0')
                  ],
                  tools: [
                        JUnit(deleteOutputFiles: true,
                              failIfNotNew: true,
                              pattern: 'test_result.xml',
                              skipNoTestFiles: false,
                              stopProcessingIfError: true)
                  ]
        	}
        }
    }
}
