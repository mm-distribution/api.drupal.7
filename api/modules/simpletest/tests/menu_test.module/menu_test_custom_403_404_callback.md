# menu_test_custom_403_404_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 397–406 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L397-L406)
- **Module/theme:** batch_test

## Signature

```php
function menu_test_custom_403_404_callback()
```

## Documentation

```text
Callback for our custom 403 and 404 pages.
```

## Code

```php
function menu_test_custom_403_404_callback() {
  // When requested by one of the MenuTrailTestCase tests, record the final
  // active trail now that the user has been redirected to the custom 403 or
  // 404 page. See menu_test_init().
  if (variable_get('menu_test_record_active_trail', FALSE)) {
    variable_set('menu_test_active_trail_final', menu_get_active_trail());
  }

  return 'This is menu_test_custom_403_404_callback().';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
