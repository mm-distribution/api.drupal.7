# index.php

- **Source:** [local](../../source/index.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/index.php) · 22 lines

## File documentation

```text
@file
The PHP page that serves all page requests on a Drupal installation.

The routines here dispatch control to the appropriate handler, which then
prints the appropriate page.

All Drupal code is released under the GNU General Public License.
See COPYRIGHT.txt and LICENSE.txt.
```

## Constants

### DRUPAL_ROOT

- Line 17

```php
define('DRUPAL_ROOT', getcwd());
```

```text
Root directory of Drupal installation.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
