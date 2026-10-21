# _form_test_tableselect_get_data()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 571–601 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L571-L601)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_tableselect_get_data()
```

## Documentation

```text
Create a header and options array. Helper function for callbacks.
```

## Code

```php
function _form_test_tableselect_get_data() {
  $header = array(
    'one' => t('One'),
    'two' => t('Two'),
    'three' => t('Three'),
    'four' => t('Four'),
  );

  $options['row1'] = array(
    'one' => 'row1col1',
    'two' => t('row1col2'),
    'three' => t('row1col3'),
    'four' => t('row1col4'),
  );

  $options['row2'] = array(
    'one' => 'row2col1',
    'two' => t('row2col2'),
    'three' => t('row2col3'),
    'four' => t('row2col4'),
  );

  $options['row3'] = array(
    'one' => 'row3col1',
    'two' => t('row3col2'),
    'three' => t('row3col3'),
    'four' => t('row3col4'),
  );

  return array($header, $options);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
