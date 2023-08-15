# Dev MaximaPool setup script

*For keepping a copy, not for serious distribution.*

This ansible playbook combined with a locally run script does the following:

 1. The local script pulls maxima-scripts from various sources and builds matching
    maxima-pool configs. To configure the sources set them in the script.
 2. The ansible playbook installs a fully functioning MaximaPool with specific SBCL 
    Maximas and then ensures that all the maxima-scripts have matching images 
    present.
 3. Should image generation need to happen it will then also reboot the Pool.
 4. The playbook also install a POST caching Nginx proxy, to use the pool without
    that cache simpy use port 8080 directly otherwise go for 80


Generally speaking these are indempotent actions and you can simply run both 
scripts in sequence at any time. So just call:

 > ./local.py; ansible-playbook poolsetup.yaml

Note that the "stackmaxima.mac" in use is hard coded and needs to be periodically
updated and matching it to particular versions of STACK is not currently handled.



## Requirements / install

 1. A virtual machine Ubuntu 22.04 "jammy"
 2. Some other machine with Ansible and rsync installed.
 3. Basic user on that other machine and SSH-key besed access as root on the VM.
    Basically, on the VM set up the roots `/root/.ssh/authorized_keys` and uncomment
    `/etc/ssh/sshd_config` line that says "PermitRootLogin prohibit-password"
 4. Full copy of this set of files on that other machine, any directory will do.
 5. Modify the local.py script so that the list of sources `SRCS` makes sense. 
    Then run `./local.py`
 6. Ensure that you have an Ansible inventory file, you ca nhave it anywhere and
    give it as an argument when running the playbook, or simply use the default one
    if the other machine is such that you can mess up things freely. Basically,
    create `/etc/ansible/hosts` and add the following within:

```
[maximapool]
my.litle.pool.com maxima_version='5.44.0,5.41.0' 
```
    
    You may define multiple machines, by having multiple lines. Note that
    `my.little.pool.com` is the bit you replace with the IP or DNS name of your
    VM and the maxima_versions is a comma separated list of maxima versions to
    install on that machine. Note that the script can only install ersions it has
    sources for, simply drop the matchin `tar.gz` into `mpfiles/opt/maxima-src` 
    and things should work.

### Advanced tuning.

 1. You can modify the `maximalocal.mac` within the local.py script, do ntoe the 
    escapes though.
 2. The default pool config can also be tuned if you are usign this for something
    else than development work, it is at `mpfiles/opt/maximapool-configs/pool.conf`.
 3. Servlet, password can be tuned at `mpfiles/opt/maximapool-servlet/servlet.conf`
 4. You could change the LISP from SBCL to something else, but then you would need
    to modify the memory image generation that is hidden as the last line of 
    "maximalocal.mac" in local.py and the config level "gen.sh" defined in that
    script.
 5. It makes sense to copy the ansible playbook and drop everythign extra out of it,
    i.e. the full maxima compilation and package installation logic is pretty much
    pointless to do every time you wish to change the config.
 6. Naturally you can also use something else than "Jammy", just change the package
    names and conditions in the playbook.
 7. Installing `haveged` is probably unnecessay, so maybe try dropping it.