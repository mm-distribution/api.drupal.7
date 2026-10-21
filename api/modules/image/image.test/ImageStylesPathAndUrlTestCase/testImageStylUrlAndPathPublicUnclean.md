# ImageStylesPathAndUrlTestCase::testImageStylUrlAndPathPublicUnclean()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 181–183 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L181-L183)
- **Class:** [ImageStylesPathAndUrlTestCase](../ImageStylesPathAndUrlTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageStylUrlAndPathPublicUnclean()
```

## Documentation

```text
Test image_style_url() with the "public://" scheme and unclean URLs.
```

## Code

```php
   function testImageStylUrlAndPathPublicUnclean() {
     $this->_testImageStyleUrlAndPath('public', FALSE);
   }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
