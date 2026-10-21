# EarlyBootstrapTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/boot.test`](../_file.md), lines 7–13 · [local source](../../../../../../source/modules/simpletest/tests/boot.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/boot.test#L7-L13)
- **Class:** [EarlyBootstrapTestCase](../EarlyBootstrapTestCase.md)
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
      'name'  => 'Early bootstrap test',
      'description'  => 'Confirm that calling module_implements() during early bootstrap does not pollute the module_implements() cache.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/boot.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/boot.test) · Licensed GPL-2.0-or-later (see LICENSE)._
