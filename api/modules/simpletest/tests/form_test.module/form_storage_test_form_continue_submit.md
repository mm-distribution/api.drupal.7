# form_storage_test_form_continue_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 853–857 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L853-L857)
- **Module/theme:** batch_test

## Signature

```php
function form_storage_test_form_continue_submit($form, &$form_state)
```

## Documentation

```text
Form submit handler to continue multi-step form.
```

## Code

```php
function form_storage_test_form_continue_submit($form, &$form_state) {
  $form_state['storage']['thing']['title'] = $form_state['values']['title'];
  $form_state['storage']['thing']['value'] = $form_state['values']['value'];
  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
