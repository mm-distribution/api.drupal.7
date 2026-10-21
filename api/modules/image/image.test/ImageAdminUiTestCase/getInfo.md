# ImageAdminUiTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 520–526 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L520-L526)
- **Class:** [ImageAdminUiTestCase](../ImageAdminUiTestCase.md)
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
      'name' => 'Administrative user interface',
      'description' => 'Tests the forms used in the administrative user interface.',
      'group' => 'Image',
    );
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
