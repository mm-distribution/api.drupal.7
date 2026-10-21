# simpletest_js_alter()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 94–101 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L94-L101)
- **Module/theme:** simpletest
- **Implements:** [hook_js_alter()](../../system/system.api.php/hook_js_alter.md)

## Signature

```php
function simpletest_js_alter(&$javascript)
```

## Documentation

```text
Implements hook_js_alter().
```

## Code

```php
function simpletest_js_alter(&$javascript) {
  // Since SimpleTest is a special use case for the table select, stick the
  // SimpleTest JavaScript above the table select.
  $simpletest = drupal_get_path('module', 'simpletest') . '/simpletest.js';
  if (array_key_exists($simpletest, $javascript) && array_key_exists('misc/tableselect.js', $javascript)) {
    $javascript[$simpletest]['weight'] = $javascript['misc/tableselect.js']['weight'] - 1;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
