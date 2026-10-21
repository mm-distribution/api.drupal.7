# batch_test_mock_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 290–300 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L290-L300)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_mock_form($form, $form_state)
```

## Documentation

```text
A simple form with a textfield and submit button.
```

## Code

```php
function batch_test_mock_form($form, $form_state) {
  $form['test_value'] = array(
    '#type' => 'textfield',
  );
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Submit'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
