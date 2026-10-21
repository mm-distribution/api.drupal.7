# simpletest_theme()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 78–89 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L78-L89)
- **Module/theme:** simpletest
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function simpletest_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function simpletest_theme() {
  return array(
    'simpletest_test_table' => array(
      'render element' => 'table',
      'file' => 'simpletest.pages.inc',
    ),
    'simpletest_result_summary' => array(
      'render element' => 'form',
      'file' => 'simpletest.pages.inc',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
