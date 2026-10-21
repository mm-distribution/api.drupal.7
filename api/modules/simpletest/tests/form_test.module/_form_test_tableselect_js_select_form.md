# _form_test_tableselect_js_select_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 682–702 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L682-L702)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_tableselect_js_select_form($form, $form_state, $action)
```

## Documentation

```text
Test functionality of the tableselect #js_select property.
```

## Code

```php
function _form_test_tableselect_js_select_form($form, $form_state, $action) {
  switch ($action) {
    case 'multiple-true-default':
      $options = array('#multiple' => TRUE);
      break;

    case 'multiple-false-default':
      $options = array('#multiple' => FALSE);
      break;

    case 'multiple-true-no-advanced-select':
      $options = array('#multiple' => TRUE, '#js_select' => FALSE);
      break;

    case 'multiple-false-advanced-select':
      $options = array('#multiple' => FALSE, '#js_select' => TRUE);
      break;
  }

  return _form_test_tableselect_form_builder($form, $form_state, $options);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
