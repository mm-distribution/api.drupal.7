# form_test_form_state_values_clean_advanced_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1112–1116 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1112-L1116)
- **Module/theme:** batch_test

## Signature

```php
function form_test_form_state_values_clean_advanced_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for form_test_form_state_values_clean_advanced_form().
```

## Code

```php
function form_test_form_state_values_clean_advanced_form_submit($form, &$form_state) {
  form_state_values_clean($form_state);
  print t('You WIN!');
  exit;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
