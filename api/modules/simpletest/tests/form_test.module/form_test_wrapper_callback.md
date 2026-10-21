# form_test_wrapper_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1042–1048 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1042-L1048)
- **Module/theme:** batch_test

## Signature

```php
function form_test_wrapper_callback($form_id)
```

## Documentation

```text
Menu callback; Invokes a form builder function with a wrapper callback.
```

## Code

```php
function form_test_wrapper_callback($form_id) {
  $form_state = array(
    'build_info' => array('args' => array()),
    'wrapper_callback' => 'form_test_wrapper_callback_wrapper',
  );
  return drupal_build_form($form_id, $form_state);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
