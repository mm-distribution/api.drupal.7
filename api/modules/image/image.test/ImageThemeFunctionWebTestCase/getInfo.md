# ImageThemeFunctionWebTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 1951–1957 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L1951-L1957)
- **Class:** [ImageThemeFunctionWebTestCase](../ImageThemeFunctionWebTestCase.md)
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
      'name' => 'Image theme functions',
      'description' => 'Test that the image theme functions work correctly.',
      'group' => 'Image',
    );
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
