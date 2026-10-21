# _form_test_tableselect_empty_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 675–677 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L675-L677)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_tableselect_empty_form($form, $form_state)
```

## Documentation

```text
Test functionality of the tableselect #empty property.
```

## Code

```php
function _form_test_tableselect_empty_form($form, $form_state) {
  return _form_test_tableselect_form_builder($form, $form_state, array('#options' => array()));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
