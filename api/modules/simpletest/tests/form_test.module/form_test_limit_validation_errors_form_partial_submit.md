# form_test_limit_validation_errors_form_partial_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 560–566 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L560-L566)
- **Module/theme:** batch_test

## Signature

```php
function form_test_limit_validation_errors_form_partial_submit($form, $form_state)
```

## Documentation

```text
Form submit handler for the partial validation submit button.
```

## Code

```php
function form_test_limit_validation_errors_form_partial_submit($form, $form_state) {
  // The title has not been validated, thus its value - in case of the test case
  // an empty string - may not be set.
  if (!isset($form_state['values']['title']) && isset($form_state['values']['test'])) {
    drupal_set_message('Only validated values appear in the form values.');
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
