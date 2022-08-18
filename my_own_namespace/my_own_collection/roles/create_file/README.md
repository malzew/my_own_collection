Role Name
=========

Simple role t create file with content.

Requirements
------------

No

Role Variables
--------------

| Variable name | Default          | Description                              |
|---------------|------------------|------------------------------------------|
| path          | "/tmp/test.txt"  | This vaiable is pah to file for creating |
| content       | "Hello world!\n" | Content of file                          |

Dependencies
------------

No

Example Playbook
----------------

    - hosts: servers
      roles:
        create_file:
            path: '/tmp/test.txt'
            content: 'Hello world!\n'


License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
