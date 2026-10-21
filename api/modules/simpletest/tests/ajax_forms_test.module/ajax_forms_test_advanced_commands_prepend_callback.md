# ajax_forms_test_advanced_commands_prepend_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 384–388 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L384-L388)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_advanced_commands_prepend_callback($form, $form_state)
```

## Documentation

```text
Ajax callback for 'prepend'.
```

## Code

```php
function ajax_forms_test_advanced_commands_prepend_callback($form, $form_state) {
  $commands = array();
  $commands[] = ajax_command_prepend('#prepend_div', "prepended text");
  return array('#type' => 'ajax', '#commands' => $commands);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
