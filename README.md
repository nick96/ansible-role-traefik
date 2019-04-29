Role Name
=========

Configurable Ansible role to deploy traefik. This role should deploy
traefik with almost no configuration with some good defaults. See
[Role Variables](#Role-Variables) for exactly which varaibles must be
configured.

Requirements
------------

Role Variables
--------------

Dependencies
------------

- ansible-role-docker

Installs docker on the target host. This does not require setting any
variables.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { 
			 role: ansible-role-traefik,
			 traefik_letsencrypt_email: example@example.com
		   }

License
-------

MIT
