# menu_test_init()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 385–392 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L385-L392)
- **Module/theme:** batch_test
- **Implements:** [hook_init()](../../../system/system.api.php/hook_init.md)

## Signature

```php
function menu_test_init()
```

## Documentation

```text
Implements hook_init().
```

## Code

```php
function menu_test_init() {
  // When requested by one of the MenuTrailTestCase tests, record the initial
  // active trail during Drupal's bootstrap (before the user is redirected to a
  // custom 403 or 404 page). See menu_test_custom_403_404_callback().
  if (variable_get('menu_test_record_active_trail', FALSE)) {
    variable_set('menu_test_active_trail_initial', menu_get_active_trail());
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
