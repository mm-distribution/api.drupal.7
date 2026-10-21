# _form_test_submit_values_json()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 263–266 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L263-L266)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_submit_values_json($form, &$form_state)
```

## Documentation

```text
Form submit handler to return form values as JSON.
```

## Code

```php
function _form_test_submit_values_json($form, &$form_state) {
  drupal_json_output($form_state['values']);
  drupal_exit();
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
