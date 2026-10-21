# ImageStylesHTTPHeadersTestCase::setUp()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 2146–2155 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L2146-L2155)
- **Class:** [ImageStylesHTTPHeadersTestCase](../ImageStylesHTTPHeadersTestCase.md)
- **Module/theme:** image

## Signature

```php
public function setUp()
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public function setUp() {
    parent::setUp('image_module_test');

    $this->styleName = 'style_foo_scale';
    $style = image_style_save(array(
      'name' => $this->styleName,
      'label' => $this->randomString(),
    ));
    $this->styleId = $style['isid'];
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
