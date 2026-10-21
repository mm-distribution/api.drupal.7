# ajax_forms_test_advanced_commands_settings_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 411–416 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L411-L416)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_advanced_commands_settings_callback($form, $form_state)
```

## Documentation

```text
Ajax callback for 'settings'.
```

## Code

```php
function ajax_forms_test_advanced_commands_settings_callback($form, $form_state) {
  $commands = array();
  $setting['ajax_forms_test']['foo'] = 42;
  $commands[] = ajax_command_settings($setting);
  return array('#type' => 'ajax', '#commands' => $commands);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
