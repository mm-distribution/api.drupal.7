# install.php

- **Source:** [local](../../source/install.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/install.php) · 27 lines

## File documentation

```text
@file
Initiates a browser-based installation of Drupal.
```

## Constants

### DRUPAL_ROOT

- Line 11

```php
define('DRUPAL_ROOT', getcwd());
```

```text
Defines the root directory of the Drupal installation.
```

### MAINTENANCE_MODE

- Line 16

```php
define('MAINTENANCE_MODE', 'install');
```

```text
Global flag to indicate the site is in installation mode.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
