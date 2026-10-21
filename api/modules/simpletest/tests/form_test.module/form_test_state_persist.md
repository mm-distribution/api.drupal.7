# form_test_state_persist()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1653–1667 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1653-L1667)
- **Module/theme:** batch_test

## Signature

```php
function form_test_state_persist($form, &$form_state)
```

## Documentation

```text
Form constructor for testing form state persistence.
```

## Code

```php
function form_test_state_persist($form, &$form_state) {
  $form['title'] = array(
    '#type' => 'textfield',
    '#title' => 'title',
    '#default_value' => 'DEFAULT',
    '#required' => TRUE,
  );
  $form_state['value'] = 'State persisted.';

  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Submit'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
