# ajax_forms_test_advanced_commands_insert_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 375–379 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L375-L379)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_advanced_commands_insert_callback($form, $form_state)
```

## Documentation

```text
Ajax callback for 'insert'.
```

## Code

```php
function ajax_forms_test_advanced_commands_insert_callback($form, $form_state) {
  $commands = array();
  $commands[] = ajax_command_insert('#insert_div', 'insert replacement text');
  return array('#type' => 'ajax', '#commands' => $commands);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
