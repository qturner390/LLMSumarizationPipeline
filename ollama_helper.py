import subprocess
import time
from typing import Optional
import requests

OLLAMA_URL = 'http://localhost:11434'


def is_ollama_running() -> bool:
    """Check if the ollama server is responding."""
    try:
        requests.get(f"{OLLAMA_URL}/api/tags", timeout=1)
        return True
    except requests.RequestException:
        return False


def start_ollama(model: str = 'llama3.2', use_serve: bool = True) -> Optional[subprocess.Popen]:
    """Start the Ollama server if it isn't running."""
    if is_ollama_running():
        return None

    cmd = ['ollama', 'serve'] if use_serve else ['ollama', 'run', model]
    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(2)
    return process


def stop_ollama(process: Optional[subprocess.Popen]) -> None:
    """Terminate the spawned Ollama process"""
    if process is None:
        return

    if process.poll() is None:
        try:
            if process.stdin:
                process.stdin.write(b'/bye\n')
                process.stdin.flush()
                process.wait(timeout=5)
        except Exception:
            process.kill()
