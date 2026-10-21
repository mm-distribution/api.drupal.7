# ImageFileMoveTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 545–551 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L545-L551)
- **Class:** [ImageFileMoveTest](../ImageFileMoveTest.md)
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
      'name' => 'Image moving',
      'description' => 'Tests the file move function for managed files.',
      'group' => 'Image',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
