# ListFieldTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 16–22 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L16-L22)
- **Class:** [ListFieldTestCase](../ListFieldTestCase.md)
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
      'name' => 'List field',
      'description' => 'Test the List field type.',
      'group' => 'Field types',
    );
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
