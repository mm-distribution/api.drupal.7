# form_test_validate_no_token()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 467–476 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L467-L476)
- **Module/theme:** batch_test

## Signature

```php
function form_test_validate_no_token($form, &$form_state)
```

## Documentation

```text
Form builder for testing submission of a form without a CSRF token.
```

## Code

```php
function form_test_validate_no_token($form, &$form_state) {
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => 'Save',
  );

  $form['#token'] = FALSE;

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
