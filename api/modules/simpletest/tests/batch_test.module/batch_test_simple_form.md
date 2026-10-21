# batch_test_simple_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 98–116 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L98-L116)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_simple_form()
```

## Documentation

```text
Simple form.
```

## Code

```php
function batch_test_simple_form() {
  $form['batch'] = array(
    '#type' => 'select',
    '#title' => 'Choose batch',
    '#options' => array(
      'batch_0' => 'batch 0',
      'batch_1' => 'batch 1',
      'batch_2' => 'batch 2',
      'batch_3' => 'batch 3',
      'batch_4' => 'batch 4',
    ),
  );
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => 'Submit',
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
