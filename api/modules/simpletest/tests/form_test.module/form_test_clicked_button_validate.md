# form_test_clicked_button_validate()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1841–1848 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1841-L1848)
- **Module/theme:** batch_test

## Signature

```php
function form_test_clicked_button_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for the form_test_clicked_button() form.
```

## Code

```php
function form_test_clicked_button_validate($form, &$form_state) {
  if (isset($form_state['triggering_element'])) {
    drupal_set_message(t('The clicked button is %name.', array('%name' => $form_state['triggering_element']['#name'])));
  }
  else {
    drupal_set_message('There is no clicked button.');
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
