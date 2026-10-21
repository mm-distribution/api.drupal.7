# form_test_validate_no_token_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 481–483 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L481-L483)
- **Module/theme:** batch_test

## Signature

```php
function form_test_validate_no_token_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for form_test_validate_no_token().
```

## Code

```php
function form_test_validate_no_token_submit($form, &$form_state) {
  drupal_set_message('The form_test_validate_no_token form has been submitted successfully.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
