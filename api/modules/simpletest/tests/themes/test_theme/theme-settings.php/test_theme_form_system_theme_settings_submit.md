# test_theme_form_system_theme_settings_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/themes/test_theme/theme-settings.php`](_file.md), lines 30–32 · [local source](../../../../../../../source/modules/simpletest/tests/themes/test_theme/theme-settings.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/themes/test_theme/theme-settings.php#L30-L32)
- **Module/theme:** test_theme

## Signature

```php
function test_theme_form_system_theme_settings_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for the test theme settings form.

@see test_theme_form_system_theme_settings_alter()
```

## Code

```php
function test_theme_form_system_theme_settings_submit($form, &$form_state) {
  drupal_set_message('The test theme setting was saved.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/themes/test_theme/theme-settings.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/themes/test_theme/theme-settings.php) · Licensed GPL-2.0-or-later (see LICENSE)._
