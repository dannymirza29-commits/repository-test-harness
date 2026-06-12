import subprocess
import json
from pathlib import Path
from datetime import datetime

class TestHarness:
    def __init__(self, repo_path: str, container_image: str):
        self.repo_path = repo_path
        self.container_image = container_image
        self.report = {}
    
    def run_tests(self) -> dict:
        """Run tests in isolated container"""
        try:
            cmd = [
                "docker", "run", "--rm",
                "-v", f"{self.repo_path}:/repo",
                self.container_image,
                "/bin/bash", "-c",
                "cd /repo && mkdir -p build && cd build && cmake .. && make && make test"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            self.report = {
                "timestamp": datetime.now().isoformat(),
                "status": "passed" if result.returncode == 0 else "failed",
                "return_code": result.returncode,
                "output": result.stdout[-500:],
            }
            
            return self.report
        
        except Exception as e:
            self.report["error"] = str(e)
            return self.report
    
    def save_report(self, output_file: str = "test_report.json"):
        """Save test report to file"""
        Path(output_file).write_text(json.dumps(self.report, indent=2))

def main():
    harness = TestHarness("/repo", "cpp-validator:latest")
    report = harness.run_tests()
    harness.save_report()
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
