# batch_test_chained_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 177–197 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L177-L197)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_chained_form()
```

## Documentation

```text
Form with chained submit callbacks.
```

## Code

```php
function batch_test_chained_form() {
  // This value is used to test that $form_state persists through batched
  // submit handlers.
  $form['value'] = array(
    '#type' => 'textfield',
    '#title' => 'Value',
    '#default_value' => 1,
  );
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => 'Submit',
  );
  $form['#submit'] = array(
    'batch_test_chained_form_submit_1',
    'batch_test_chained_form_submit_2',
    'batch_test_chained_form_submit_3',
    'batch_test_chained_form_submit_4',
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
