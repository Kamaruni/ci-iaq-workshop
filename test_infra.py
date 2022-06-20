def test_docker_is_installed(host):
    docker = host.package("docker-ce")
    assert docker.is_installed
