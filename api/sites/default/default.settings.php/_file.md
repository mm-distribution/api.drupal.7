# sites/default/default.settings.php

- **Source:** [local](../../../../source/sites/default/default.settings.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/sites/default/default.settings.php) · 933 lines

## File documentation

```text
@file
Drupal site-specific configuration file.

IMPORTANT NOTE:
This file may have been set to read-only by the Drupal installation program.
If you make changes to this file, be sure to protect it again after making
your modifications. Failure to remove write permissions to this file is a
security risk.

The configuration file to be loaded is based upon the rules below. However
if the multisite aliasing file named sites/sites.php is present, it will be
loaded, and the aliases in the array $sites will override the default
directory rules below. See sites/example.sites.php for more information about
aliases.

The configuration directory will be discovered by stripping the website's
hostname from left to right and pathname from right to left. The first
configuration file found will be used and any others will be ignored. If no
other configuration file is found then the default configuration file at
'sites/default' will be used.

For example, for a fictitious site installed at
http://www.drupal.org:8080/mysite/test/, the 'settings.php' file is searched
for in the following directories:

- sites/8080.www.drupal.org.mysite.test
- sites/www.drupal.org.mysite.test
- sites/drupal.org.mysite.test
- sites/org.mysite.test

- sites/8080.www.drupal.org.mysite
- sites/www.drupal.org.mysite
- sites/drupal.org.mysite
- sites/org.mysite

- sites/8080.www.drupal.org
- sites/www.drupal.org
- sites/drupal.org
- sites/org

- sites/default

Note that if you are installing on a non-standard port number, prefix the
hostname with that number. For example,
http://www.drupal.org:8080/mysite/test/ could be loaded from
sites/8080.www.drupal.org.mysite.test/.

@see example.sites.php
@see conf_path()
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
