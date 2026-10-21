# form_test_wrapper_callback_wrapper()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1053–1056 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1053-L1056)
- **Module/theme:** batch_test

## Signature

```php
function form_test_wrapper_callback_wrapper($form, &$form_state)
```

## Documentation

```text
Form wrapper for form_test_wrapper_callback_form().
```

## Code

```php
function form_test_wrapper_callback_wrapper($form, &$form_state) {
  $form['wrapper'] = array('#markup' => 'Form wrapper callback element output.');
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
