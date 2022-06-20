def test_docker_is_installed(host):
    docker = host.package("docker-ce")
    assert docker.is_installed

def test_app_is_running(host):
    app = host.docker("my-hero-app")
    assert app.is_running
