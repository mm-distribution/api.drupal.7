# form_test_redirect_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1885–1892 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1885-L1892)
- **Module/theme:** batch_test

## Signature

```php
function form_test_redirect_submit(&$form, &$form_state)
```

## Documentation

```text
Form submit handler to test different redirect behaviours.
```

## Code

```php
function form_test_redirect_submit(&$form, &$form_state) {
  if (!empty($form_state['values']['redirection'])) {
    $form_state['redirect'] = !empty($form_state['values']['destination']) ? $form_state['values']['destination'] : NULL;
  }
  else {
    $form_state['redirect'] = FALSE;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
