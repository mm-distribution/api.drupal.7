# scripts/dump-database-d7.sh

- **Source:** [local](../../../source/scripts/dump-database-d7.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/dump-database-d7.sh) · 91 lines

## File documentation

```text
@file
Dumps a Drupal 7 database into a PHP script to test the upgrade process.

Run this script at the root of an existing Drupal 7 installation.

The output of this script is a PHP script that can be run inside Drupal 7
and recreates the Drupal 7 database as dumped. Transient data from cache,
session, and watchdog tables are not recorded.
```

## Constants

### DRUPAL_ROOT

- Line 16

```php
define('DRUPAL_ROOT', getcwd());
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
