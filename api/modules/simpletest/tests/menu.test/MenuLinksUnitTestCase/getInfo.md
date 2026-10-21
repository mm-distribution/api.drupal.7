# MenuLinksUnitTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 678–684 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L678-L684)
- **Class:** [MenuLinksUnitTestCase](../MenuLinksUnitTestCase.md)
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
      'name' => 'Menu links',
      'description' => 'Test handling of menu links hierarchies.',
      'group' => 'Menu',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
