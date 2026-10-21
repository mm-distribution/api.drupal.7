# _form_test_input_forgery_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1567–1570 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1567-L1570)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_input_forgery_submit($form, &$form_state)
```

## Documentation

```text
Return the form values via JSON.
```

## Code

```php
function _form_test_input_forgery_submit($form, &$form_state) {
  drupal_json_output($form_state['values']);
  exit();
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
