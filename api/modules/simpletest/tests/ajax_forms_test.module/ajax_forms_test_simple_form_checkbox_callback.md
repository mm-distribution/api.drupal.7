# ajax_forms_test_simple_form_checkbox_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 86–91 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L86-L91)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_simple_form_checkbox_callback($form, $form_state)
```

## Documentation

```text
Ajax callback triggered by checkbox.
```

## Code

```php
function ajax_forms_test_simple_form_checkbox_callback($form, $form_state) {
  $commands = array();
  $commands[] = ajax_command_html('#ajax_checkbox_value', (int) $form_state['values']['checkbox']);
  $commands[] = ajax_command_data('#ajax_checkbox_value', 'form_state_value_select', (int) $form_state['values']['checkbox']);
  return array('#type' => 'ajax', '#commands' => $commands);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
