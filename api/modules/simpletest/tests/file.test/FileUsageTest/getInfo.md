# FileUsageTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2264–2270 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2264-L2270)
- **Class:** [FileUsageTest](../FileUsageTest.md)
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
      'name' => 'File usage',
      'description' => 'Tests the file usage functions.',
      'group' => 'File',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
