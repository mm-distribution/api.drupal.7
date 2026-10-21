# ImageStylesPathAndUrlTestCase::testImageStyleUrlExtraSlash()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 195–197 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L195-L197)
- **Class:** [ImageStylesPathAndUrlTestCase](../ImageStylesPathAndUrlTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageStyleUrlExtraSlash()
```

## Documentation

```text
Test image_style_url() with a file URL that has an extra slash in it.
```

## Code

```php
  function testImageStyleUrlExtraSlash() {
    $this->_testImageStyleUrlAndPath('public', TRUE, TRUE);
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
