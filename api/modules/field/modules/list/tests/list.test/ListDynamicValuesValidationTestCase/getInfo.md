# ListDynamicValuesValidationTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 170–176 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L170-L176)
- **Class:** [ListDynamicValuesValidationTestCase](../ListDynamicValuesValidationTestCase.md)
- **Module/theme:** list_test

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
      'name' => 'List field dynamic values',
      'description' => 'Test the List field allowed values function.',
      'group' => 'Field types',
    );
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
