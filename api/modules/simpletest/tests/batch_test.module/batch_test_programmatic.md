# batch_test_programmatic()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 259–265 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L259-L265)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_programmatic($value = 1)
```

## Documentation

```text
Menu callback: programmatically submits the 'Chained' form.
```

## Code

```php
function batch_test_programmatic($value = 1) {
  $form_state = array(
    'values' => array('value' => $value)
  );
  drupal_form_submit('batch_test_chained_form', $form_state);
  return 'Got out of a programmatic batched form.';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
