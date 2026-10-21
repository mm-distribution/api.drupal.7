# PathSaveTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 352–358 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L352-L358)
- **Class:** [PathSaveTest](../PathSaveTest.md)
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
      'name' => t('Path save'),
      'description' => t('Tests that path_save() exposes the previous alias value.'),
      'group' => t('Path API'),
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
