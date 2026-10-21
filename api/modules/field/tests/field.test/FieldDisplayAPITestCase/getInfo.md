# FieldDisplayAPITestCase::getInfo()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2182–2188 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2182-L2188)
- **Class:** [FieldDisplayAPITestCase](../FieldDisplayAPITestCase.md)
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
      'name' => 'Field Display API tests',
      'description' => 'Test the display API.',
      'group' => 'Field API',
    );
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
