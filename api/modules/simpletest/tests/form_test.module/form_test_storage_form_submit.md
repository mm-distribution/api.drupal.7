# form_test_storage_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 862–869 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L862-L869)
- **Module/theme:** batch_test

## Signature

```php
function form_test_storage_form_submit($form, &$form_state)
```

## Documentation

```text
Form submit handler to finish multi-step form.
```

## Code

```php
function form_test_storage_form_submit($form, &$form_state) {
  drupal_set_message("Title: " . check_plain($form_state['values']['title']));
  drupal_set_message("Form constructions: " . $_SESSION['constructions']);
  if (isset($form_state['storage']['thing']['changed'])) {
    drupal_set_message("The thing has been changed.");
  }
  $form_state['redirect'] = 'node';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
