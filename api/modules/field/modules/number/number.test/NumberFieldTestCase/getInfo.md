# NumberFieldTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/field/modules/number/number.test`](../_file.md), lines 16–22 · [local source](../../../../../../../source/modules/field/modules/number/number.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.test#L16-L22)
- **Class:** [NumberFieldTestCase](../NumberFieldTestCase.md)
- **Module/theme:** number

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
      'name'  => 'Number field',
      'description'  => 'Test the creation of number fields.',
      'group' => 'Field types'
    );
  }
```

---
_Drupal 7.103 · [modules/field/modules/number/number.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.test) · Licensed GPL-2.0-or-later (see LICENSE)._
