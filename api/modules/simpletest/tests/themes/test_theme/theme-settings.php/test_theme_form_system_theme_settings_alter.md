# test_theme_form_system_theme_settings_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/themes/test_theme/theme-settings.php`](_file.md), lines 11–23 · [local source](../../../../../../../source/modules/simpletest/tests/themes/test_theme/theme-settings.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/themes/test_theme/theme-settings.php#L11-L23)
- **Module/theme:** test_theme
- **Implements:** [hook_form_FORM_ID_alter()](../../../../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function test_theme_form_system_theme_settings_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function test_theme_form_system_theme_settings_alter(&$form, &$form_state) {
  $form['test_theme_checkbox'] = array(
    '#type' => 'checkbox',
    '#title' => 'Test theme checkbox',
    '#default_value' => theme_get_setting('test_theme_checkbox'),
  );

  // Force the form to be cached so we can test that this file is properly
  // loaded and the custom submit handler is properly called even on a cached
  // form build.
  $form_state['cache'] = TRUE;
  $form['#submit'][] = 'test_theme_form_system_theme_settings_submit';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/themes/test_theme/theme-settings.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/themes/test_theme/theme-settings.php) · Licensed GPL-2.0-or-later (see LICENSE)._
