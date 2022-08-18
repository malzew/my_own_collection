#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os.path

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This is my own module for homework 8.4

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    path:
        description: This is path to file for wriiting
        required: true
        type: str
    content:
        desctoption: Content of file
        required: true
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_own_namespace.my_own_collection.my_doc_fragment_name

author:
    - Andrey Maltsev (https://github.com/malzew)
'''

EXAMPLES = r'''
# Pass in a path /tmp/text.txt
# Pass in content 'Some filling'
$ cat /tmp/text.txt
Some filling

# fail the module
- path: some existing file

'''

RETURN = r'''
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'file was created', 'file exists'
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)


    if not os.path.exists(module.params['path']):
        try:
            with open(module.params['path'],'w') as f:
                f.write(module.params['content'])
            result['changed'] = True
            result['message'] = 'file was created'
        except:
            module.fail_json(msg='File does not exists, but cannot create it for writing', **result)
    else:
        result['changed'] = False
        result['message'] = 'file exists'

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
