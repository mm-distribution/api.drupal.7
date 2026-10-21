# scripts/generate-d7-content.sh

- **Source:** [local](../../../source/scripts/generate-d7-content.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/generate-d7-content.sh) · 321 lines

## File documentation

```text
@file
Generates content for a Drupal 7 database to test the upgrade process.

Run this script at the root of an existing Drupal 6 installation.
Steps to use this generation script:
- Install drupal 7.
- Run this script from your Drupal ROOT directory.
- Use the dump-database-d7.sh to generate the D7 file
  modules/simpletest/tests/upgrade/database.filled.php
```

## Constants

### DRUPAL_ROOT

- Line 18

```php
define('DRUPAL_ROOT', getcwd());
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
