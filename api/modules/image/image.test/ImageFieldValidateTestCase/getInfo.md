# ImageFieldValidateTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 1249–1255 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L1249-L1255)
- **Class:** [ImageFieldValidateTestCase](../ImageFieldValidateTestCase.md)
- **Module/theme:** image

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
      'name' => 'Image field validation tests',
      'description' => 'Tests validation functions such as min/max resolution.',
      'group' => 'Image',
    );
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
