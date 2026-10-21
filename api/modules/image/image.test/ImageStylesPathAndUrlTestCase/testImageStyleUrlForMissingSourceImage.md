# ImageStylesPathAndUrlTestCase::testImageStyleUrlForMissingSourceImage()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 202–207 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L202-L207)
- **Class:** [ImageStylesPathAndUrlTestCase](../ImageStylesPathAndUrlTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageStyleUrlForMissingSourceImage()
```

## Documentation

```text
Test that an invalid source image returns a 404.
```

## Code

```php
  function testImageStyleUrlForMissingSourceImage() {
    $non_existent_uri = 'public://foo.png';
    $generated_url = image_style_url($this->style_name, $non_existent_uri);
    $this->drupalGet($generated_url);
    $this->assertResponse(404, 'Accessing an image style URL with a source image that does not exist provides a 404 error response.');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
