# ImageAdminStylesUnitTest::getImageCount()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 605–607 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L605-L607)
- **Class:** [ImageAdminStylesUnitTest](../ImageAdminStylesUnitTest.md)
- **Module/theme:** image

## Signature

```php
function getImageCount($style)
```

## Documentation

```text
Count the number of images currently create for a style.
```

## Code

```php
  function getImageCount($style) {
    return count(file_scan_directory('public://styles/' . $style['name'], '/.*/'));
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
