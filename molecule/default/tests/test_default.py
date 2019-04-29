import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hosts_file(host):
    f = host.file("/etc/hosts")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


@pytest.mark.parametrize("direcotry", ["/etc/traefik/"])
def test_directory_exist(host, directory):
    d = host.directory(directory)
    assert d.exists


@pytest.mark.parametrize(
    "file",
    [
        "/etc/traefik/.htpasswd",
        "/etc/traefik/acme.json",
        "/etc/traefik/traefik.toml",
    ],
)
def test_file_exist(host, file):
    f = host.file(file)
    assert f.exists


@pytest.mark.parametrize("file", ["web"])
def test_docker_network_exist(host, network):
    pass


@pytest.mark.parametrize("network", "containers", [("web", ["traefik"])])
def test_container_in_network(host, network, containers):
    pass


@pytest.mark.parametrize("container", ["traefik"])
def test_container_volumes(container):
    pass


@pytest.mark.parametrize("container", "ports", [("traefik", ["8080"])])
def test_container_ports_exposed(container, ports):
    pass


@pytest.mark.parametrize(
    "container", "ports", [("traefik", ["80:80", "443:443"])]
)
def test_container_ports(container, ports):
    pass


@pytest.mark.parametrize(
    "container",
    "labels",
    [
        (
            "traefik",
            {
                "traefik.enable": True,
                "traefik.port": 8080,
                "traefik.frontend.rule": "Host:traefik.localhost",
                "traefik.docker.network": "web",
                "treafik.frontend.auth.basic.userFile":
                "/etc/traefik/.htpasswd",
            },
        )
    ],
)
def test_container_labels(container, labels):
    pass
