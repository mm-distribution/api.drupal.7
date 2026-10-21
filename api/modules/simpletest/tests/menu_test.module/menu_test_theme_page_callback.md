# menu_test_theme_page_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 418–430 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L418-L430)
- **Module/theme:** batch_test

## Signature

```php
function menu_test_theme_page_callback($inherited = FALSE)
```

## Documentation

```text
Page callback to use when testing the theme callback functionality.

@param $inherited
  An optional boolean to set to TRUE when the requested page is intended to
  inherit the theme of its parent.
@return
  A string describing the requested custom theme and actual theme being used
  for the current page request.
```

## Code

```php
function menu_test_theme_page_callback($inherited = FALSE) {
  global $theme_key;
  // Initialize the theme system so that $theme_key will be populated.
  drupal_theme_initialize();
  // Now check both the requested custom theme and the actual theme being used.
  $custom_theme = menu_get_custom_theme();
  $requested_theme = empty($custom_theme) ? 'NONE' : $custom_theme;
  $output = "Custom theme: $requested_theme. Actual theme: $theme_key.";
  if ($inherited) {
    $output .= ' Theme callback inheritance is being tested.';
  }
  return $output;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
