# ajax_forms_test_simple_form_select_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 76–81 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L76-L81)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_simple_form_select_callback($form, $form_state)
```

## Documentation

```text
Ajax callback triggered by select.
```

## Code

```php
function ajax_forms_test_simple_form_select_callback($form, $form_state) {
  $commands = array();
  $commands[] = ajax_command_html('#ajax_selected_color', $form_state['values']['select']);
  $commands[] = ajax_command_data('#ajax_selected_color', 'form_state_value_select', $form_state['values']['select']);
  return array('#type' => 'ajax', '#commands' => $commands);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
