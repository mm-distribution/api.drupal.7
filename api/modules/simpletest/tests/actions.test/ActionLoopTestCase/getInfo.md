# ActionLoopTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/actions.test`](../_file.md), lines 70–76 · [local source](../../../../../../source/modules/simpletest/tests/actions.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions.test#L70-L76)
- **Class:** [ActionLoopTestCase](../ActionLoopTestCase.md)
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
      'name' => 'Actions executing in a potentially infinite loop',
      'description' => 'Tests actions executing in a loop, and makes sure they abort properly.',
      'group' => 'Actions',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/actions.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions.test) · Licensed GPL-2.0-or-later (see LICENSE)._
