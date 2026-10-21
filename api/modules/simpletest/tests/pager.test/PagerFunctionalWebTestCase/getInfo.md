# PagerFunctionalWebTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/pager.test`](../_file.md), lines 15–21 · [local source](../../../../../../source/modules/simpletest/tests/pager.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/pager.test#L15-L21)
- **Class:** [PagerFunctionalWebTestCase](../PagerFunctionalWebTestCase.md)
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
      'name' => 'Pager functionality',
      'description' => 'Tests pager functionality.',
      'group' => 'Pager',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/pager.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/pager.test) · Licensed GPL-2.0-or-later (see LICENSE)._
