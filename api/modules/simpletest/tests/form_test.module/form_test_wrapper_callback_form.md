# form_test_wrapper_callback_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1061–1064 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1061-L1064)
- **Module/theme:** batch_test

## Signature

```php
function form_test_wrapper_callback_form($form, &$form_state)
```

## Documentation

```text
Form builder for form wrapper callback test.
```

## Code

```php
function form_test_wrapper_callback_form($form, &$form_state) {
  $form['builder'] = array('#markup' => 'Form builder element output.');
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
