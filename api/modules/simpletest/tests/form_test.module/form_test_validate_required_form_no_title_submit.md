# form_test_validate_required_form_no_title_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 460–462 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L460-L462)
- **Module/theme:** batch_test

## Signature

```php
function form_test_validate_required_form_no_title_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for form_test_validate_required_form_no_title().
```

## Code

```php
function form_test_validate_required_form_no_title_submit($form, &$form_state) {
  drupal_set_message('The form_test_validate_required_form_no_title form was submitted successfully.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
