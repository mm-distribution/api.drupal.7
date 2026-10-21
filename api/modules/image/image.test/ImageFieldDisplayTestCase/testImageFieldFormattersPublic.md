# ImageFieldDisplayTestCase::testImageFieldFormattersPublic()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 953–955 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L953-L955)
- **Class:** [ImageFieldDisplayTestCase](../ImageFieldDisplayTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageFieldFormattersPublic()
```

## Documentation

```text
Test image formatters on node display for public files.
```

## Code

```php
  function testImageFieldFormattersPublic() {
    $this->_testImageFieldFormatters('public');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
