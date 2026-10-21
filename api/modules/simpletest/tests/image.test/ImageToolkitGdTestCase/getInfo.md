# ImageToolkitGdTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 219–225 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L219-L225)
- **Class:** [ImageToolkitGdTestCase](../ImageToolkitGdTestCase.md)
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
      'name' => 'Image GD manipulation tests',
      'description' => 'Check that core image manipulations work properly: scale, resize, rotate, crop, scale and crop, and desaturate.',
      'group' => 'Image',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
