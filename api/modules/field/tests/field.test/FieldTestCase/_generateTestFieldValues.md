# FieldTestCase::_generateTestFieldValues()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 38–45 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L38-L45)
- **Class:** [FieldTestCase](../FieldTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function _generateTestFieldValues($cardinality)
```

## Documentation

```text
Generate random values for a field_test field.

@param $cardinality
  Number of values to generate.
@return
 An array of random values, in the format expected for field values.
```

## Code

```php
  function _generateTestFieldValues($cardinality) {
    $values = array();
    for ($i = 0; $i < $cardinality; $i++) {
      // field_test fields treat 0 as 'empty value'.
      $values[$i]['value'] = mt_rand(1, 127);
    }
    return $values;
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
