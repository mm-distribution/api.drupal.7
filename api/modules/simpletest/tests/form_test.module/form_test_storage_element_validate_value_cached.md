# form_test_storage_element_validate_value_cached()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 840–848 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L840-L848)
- **Module/theme:** batch_test

## Signature

```php
function form_test_storage_element_validate_value_cached($element, &$form_state)
```

## Documentation

```text
Form element validation handler for 'value' element in form_test_storage_form().

Tests updating of cached form storage during validation.
```

## Code

```php
function form_test_storage_element_validate_value_cached($element, &$form_state) {
  // If caching is enabled and we receive a certain value, change the storage.
  // This presumes that another submitted form value triggers a validation error
  // elsewhere in the form. Form API should still update the cached form storage
  // though.
  if (isset($_REQUEST['cache']) && $form_state['values']['value'] == 'change_title') {
    $form_state['storage']['thing']['changed'] = TRUE;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
