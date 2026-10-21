# menu_test_theme_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 440–456 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L440-L456)
- **Module/theme:** batch_test

## Signature

```php
function menu_test_theme_callback($argument)
```

## Documentation

```text
Theme callback to use when testing the theme callback functionality.

@param $argument
  The argument passed in from the URL.
@return
  The name of the custom theme to request for the current page.
```

## Code

```php
function menu_test_theme_callback($argument) {
  // Test using the variable administrative theme.
  if ($argument == 'use-admin-theme') {
    return variable_get('admin_theme');
  }
  // Test using a theme that exists, but may or may not be enabled.
  elseif ($argument == 'use-stark-theme') {
    return 'stark';
  }
  // Test using a theme that does not exist.
  elseif ($argument == 'use-fake-theme') {
    return 'fake_theme';
  }
  // For any other value of the URL argument, do not return anything. This
  // allows us to test that returning nothing from a theme callback function
  // causes the page to correctly fall back on using the main site theme.
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
