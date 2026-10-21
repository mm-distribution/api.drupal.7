# FieldInfoTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1250–1256 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1250-L1256)
- **Class:** [FieldInfoTestCase](../FieldInfoTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Field info tests',
      'description' => 'Get information about existing fields, instances and bundles.',
      'group' => 'Field API',
    );
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
