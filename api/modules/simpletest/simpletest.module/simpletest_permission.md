# simpletest_permission()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 66–73 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L66-L73)
- **Module/theme:** simpletest
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function simpletest_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function simpletest_permission() {
  return array(
    'administer unit tests' => array(
      'title' => t('Administer tests'),
      'restrict access' => TRUE,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
