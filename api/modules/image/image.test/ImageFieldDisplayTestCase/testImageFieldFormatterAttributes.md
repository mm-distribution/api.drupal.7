# ImageFieldDisplayTestCase::testImageFieldFormatterAttributes()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 1125–1137 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L1125-L1137)
- **Class:** [ImageFieldDisplayTestCase](../ImageFieldDisplayTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageFieldFormatterAttributes()
```

## Documentation

```text
Test passing attributes into the image field formatters.
```

## Code

```php
  function testImageFieldFormatterAttributes() {
    $image = theme('image_formatter', array(
      'item' => array(
        'uri' => 'http://example.com/example.png',
        'attributes' => array(
          'data-image-field-formatter' => 'testFound',
        ),
        'alt' => t('Image field formatter attribute test.'),
        'title' => t('Image field formatter'),
      ),
    ));
    $this->assertTrue(stripos($image, 'testFound') > 0, 'Image field formatters can have attributes.');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
