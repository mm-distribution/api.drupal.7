# ImageStylesPathAndUrlTestCase::testImageStyleUrlAndPathPublic()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 167–169 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L167-L169)
- **Class:** [ImageStylesPathAndUrlTestCase](../ImageStylesPathAndUrlTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageStyleUrlAndPathPublic()
```

## Documentation

```text
Test image_style_url() with a file using the "public://" scheme.
```

## Code

```php
  function testImageStyleUrlAndPathPublic() {
    $this->_testImageStyleUrlAndPath('public');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
