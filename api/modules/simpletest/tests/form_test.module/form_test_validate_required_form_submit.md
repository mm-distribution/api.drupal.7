# form_test_validate_required_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 440–442 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L440-L442)
- **Module/theme:** batch_test

## Signature

```php
function form_test_validate_required_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for form_test_validate_required_form().
```

## Code

```php
function form_test_validate_required_form_submit($form, &$form_state) {
  drupal_set_message('The form_test_validate_required_form form was submitted successfully.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
