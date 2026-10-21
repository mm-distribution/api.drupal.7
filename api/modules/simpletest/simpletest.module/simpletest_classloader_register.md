# simpletest_classloader_register()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 411–424 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L411-L424)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_classloader_register()
```

## Documentation

_No docblock in source._

## Code

```php
function simpletest_classloader_register() {

  // Prevent duplicate classloader registration.
  static $first_run = TRUE;
  if (!$first_run) {
    return;
  }
  $first_run = FALSE;

  // Only register PSR-0 class loading if we are on PHP 5.3 or higher.
  if (version_compare(PHP_VERSION, '5.3') > 0) {
    spl_autoload_register('_simpletest_autoload_psr4_psr0');
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
