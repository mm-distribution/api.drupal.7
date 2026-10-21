# ImageStylesHTTPHeadersTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 2135–2141 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L2135-L2141)
- **Class:** [ImageStylesHTTPHeadersTestCase](../ImageStylesHTTPHeadersTestCase.md)
- **Module/theme:** image

## Signature

```php
public static function getInfo()
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Image styles HTTP headers tests',
      'description' => 'Tests file size, dimensions and HTTP headers of image styles generated with scaling.',
      'group' => 'Image',
    );
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
