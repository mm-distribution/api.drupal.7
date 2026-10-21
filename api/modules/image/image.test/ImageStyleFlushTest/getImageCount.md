# ImageStyleFlushTest::getImageCount()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 2043–2045 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L2043-L2045)
- **Class:** [ImageStyleFlushTest](../ImageStyleFlushTest.md)
- **Module/theme:** image

## Signature

```php
function getImageCount($style, $wrapper)
```

## Documentation

```text
Count the number of images currently created for a style in a wrapper.
```

## Code

```php
  function getImageCount($style, $wrapper) {
    return count(file_scan_directory($wrapper . '://styles/' . $style['name'], '/.*/'));
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
