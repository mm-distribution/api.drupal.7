# ajax_forms_test_advanced_commands_after_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 277–283 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L277-L283)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_advanced_commands_after_callback($form, $form_state)
```

## Documentation

```text
Ajax callback for 'after'.
```

## Code

```php
function ajax_forms_test_advanced_commands_after_callback($form, $form_state) {
  $selector = '#after_div';

  $commands = array();
  $commands[] = ajax_command_after($selector, "This will be placed after");
  return array('#type' => 'ajax', '#commands' => $commands);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
