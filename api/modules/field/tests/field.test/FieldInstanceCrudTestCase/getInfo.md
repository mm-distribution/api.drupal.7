# FieldInstanceCrudTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2925–2931 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2925-L2931)
- **Class:** [FieldInstanceCrudTestCase](../FieldInstanceCrudTestCase.md)
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
      'name' => 'Field instance CRUD tests',
      'description' => 'Create field entities by attaching fields to entities.',
      'group' => 'Field API',
    );
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
