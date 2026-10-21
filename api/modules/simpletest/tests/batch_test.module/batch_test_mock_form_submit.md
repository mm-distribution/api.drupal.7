# batch_test_mock_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 305–307 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L305-L307)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_mock_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for the batch_test_mock form.
```

## Code

```php
function batch_test_mock_form_submit($form, &$form_state) {
  batch_test_stack('mock form submitted with value = ' . $form_state['values']['test_value']);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
