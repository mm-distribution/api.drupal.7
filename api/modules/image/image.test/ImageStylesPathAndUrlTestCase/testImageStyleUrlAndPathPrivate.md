# ImageStylesPathAndUrlTestCase::testImageStyleUrlAndPathPrivate()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 174–176 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L174-L176)
- **Class:** [ImageStylesPathAndUrlTestCase](../ImageStylesPathAndUrlTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageStyleUrlAndPathPrivate()
```

## Documentation

```text
Test image_style_url() with a file using the "private://" scheme.
```

## Code

```php
  function testImageStyleUrlAndPathPrivate() {
    $this->_testImageStyleUrlAndPath('private');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
