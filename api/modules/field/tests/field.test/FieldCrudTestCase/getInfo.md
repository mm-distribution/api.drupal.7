# FieldCrudTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2382–2388 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2382-L2388)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
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
      'name' => 'Field CRUD tests',
      'description' => 'Test field create, read, update, and delete.',
      'group' => 'Field API',
    );
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
