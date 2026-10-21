# _form_test_tableselect_ajax_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 737–739 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L737-L739)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_tableselect_ajax_callback($form, &$form_state)
```

## Documentation

```text
Ajax callback that returns the form element.
```

## Code

```php
function _form_test_tableselect_ajax_callback($form, &$form_state) {
  return $form['tableselect'];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
