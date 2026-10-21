# FieldUpdatePathTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/update.field.test`](../_file.md), lines 12–18 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/update.field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.field.test#L12-L18)
- **Class:** [FieldUpdatePathTestCase](../FieldUpdatePathTestCase.md)
- **Module/theme:** batch_test

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
      'name' => 'Field update path',
      'description' => 'Field update path tests.',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/update.field.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
