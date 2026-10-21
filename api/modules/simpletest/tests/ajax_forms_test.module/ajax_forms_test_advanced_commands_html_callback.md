# ajax_forms_test_advanced_commands_html_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 366–370 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L366-L370)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_advanced_commands_html_callback($form, $form_state)
```

## Documentation

```text
Ajax callback for 'html'.
```

## Code

```php
function ajax_forms_test_advanced_commands_html_callback($form, $form_state) {
  $commands = array();
  $commands[] = ajax_command_html('#html_div', 'replacement text');
  return array('#type' => 'ajax', '#commands' => $commands);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
