# form_test_form_state_values_clean_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1085–1089 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1085-L1089)
- **Module/theme:** batch_test

## Signature

```php
function form_test_form_state_values_clean_form_submit($form, &$form_state)
```

## Documentation

```text
Form submit handler for form_state_values_clean() test form.
```

## Code

```php
function form_test_form_state_values_clean_form_submit($form, &$form_state) {
  form_state_values_clean($form_state);
  drupal_json_output($form_state['values']);
  exit;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
