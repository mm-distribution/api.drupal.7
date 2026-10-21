# ImageStylesPathAndUrlTestCase::setUp()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 143–148 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L143-L148)
- **Class:** [ImageStylesPathAndUrlTestCase](../ImageStylesPathAndUrlTestCase.md)
- **Module/theme:** image

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('image_module_test');

    $this->style_name = 'style_foo';
    image_style_save(array('name' => $this->style_name, 'label' => $this->randomString()));
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
