Think of it like python virtualenv for vagrant...

Documentation is TODO..

# QuickStart

Install it:

```bash
$ pip install pyvagrant
```

Do things

```python
from pyvagrant import Vagrant
vagrant = Vagrant()

# Create new env
env = vagrant.environments.new("myenv")

# List environments
list(vagrant.environments)

# List boxes
list(vagrant.boxes)

# Search for a box in vagrant cloud
vagrant.search("FreeBSD")

# Search for a box in vagrant cloud for a specific provider
search_results = vagrant.search("FreeBSD", provider="vmware_desktop")

# Download a vagrant box from your search results
search_results[0].add()

# List your new boxes
print(vagrant.boxes)

# Change your default provider
vagrant.default_provider = "vmware_desktop"
```
