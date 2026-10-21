# EntityPropertiesTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3837–3843 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3837-L3843)
- **Class:** [EntityPropertiesTestCase](../EntityPropertiesTestCase.md)
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
      'name' => 'Entity properties',
      'description' => 'Tests entity properties.',
      'group' => 'Entity API',
    );
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
