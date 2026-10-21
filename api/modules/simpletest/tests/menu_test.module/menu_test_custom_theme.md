# menu_test_custom_theme()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 464–471 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L464-L471)
- **Module/theme:** batch_test
- **Implements:** [hook_custom_theme()](../../../system/system.api.php/hook_custom_theme.md)

## Signature

```php
function menu_test_custom_theme()
```

## Documentation

```text
Implement hook_custom_theme().

@return
  The name of the custom theme to use for the current page.
```

## Code

```php
function menu_test_custom_theme() {
  // If an appropriate variable has been set in the database, request the theme
  // that is stored there. Otherwise, do not attempt to dynamically set the
  // theme.
  if ($theme = variable_get('menu_test_hook_custom_theme_name', FALSE)) {
    return $theme;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
