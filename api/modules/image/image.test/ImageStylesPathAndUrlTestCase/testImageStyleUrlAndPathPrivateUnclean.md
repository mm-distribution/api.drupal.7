# ImageStylesPathAndUrlTestCase::testImageStyleUrlAndPathPrivateUnclean()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 188–190 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L188-L190)
- **Class:** [ImageStylesPathAndUrlTestCase](../ImageStylesPathAndUrlTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageStyleUrlAndPathPrivateUnclean()
```

## Documentation

```text
Test image_style_url() with the "private://" schema and unclean URLs.
```

## Code

```php
  function testImageStyleUrlAndPathPrivateUnclean() {
    $this->_testImageStyleUrlAndPath('private', FALSE);
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
