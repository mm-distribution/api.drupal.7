# form_test_programmatic_form_validate()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1763–1767 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1763-L1767)
- **Module/theme:** batch_test

## Signature

```php
function form_test_programmatic_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for programmatic form submissions.

To test that the validation handler is correctly executed, the field value is
explicitly required here.
```

## Code

```php
function form_test_programmatic_form_validate($form, &$form_state) {
  if (empty($form_state['values']['textfield'])) {
    form_set_error('textfield', t('Textfield is required.'));
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
