# _form_test_checkboxes_zero_no_redirect()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1990–1992 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1990-L1992)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_checkboxes_zero_no_redirect($form, &$form_state)
```

## Documentation

_No docblock in source._

## Code

```php
function _form_test_checkboxes_zero_no_redirect($form, &$form_state) {
  $form_state['redirect'] = FALSE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
