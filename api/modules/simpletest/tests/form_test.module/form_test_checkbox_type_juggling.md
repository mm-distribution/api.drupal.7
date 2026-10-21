# form_test_checkbox_type_juggling()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1953–1960 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1953-L1960)
- **Module/theme:** batch_test

## Signature

```php
function form_test_checkbox_type_juggling($form, $form_state, $default_value, $return_value)
```

## Documentation

_No docblock in source._

## Code

```php
function form_test_checkbox_type_juggling($form, $form_state, $default_value, $return_value) {
  $form['checkbox'] = array(
    '#type' => 'checkbox',
    '#return_value' => $return_value,
    '#default_value' => $default_value,
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
