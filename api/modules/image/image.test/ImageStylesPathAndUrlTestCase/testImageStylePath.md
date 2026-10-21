# ImageStylesPathAndUrlTestCase::testImageStylePath()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 153–162 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L153-L162)
- **Class:** [ImageStylesPathAndUrlTestCase](../ImageStylesPathAndUrlTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageStylePath()
```

## Documentation

```text
Test image_style_path().
```

## Code

```php
  function testImageStylePath() {
    $scheme = 'public';
    $actual = image_style_path($this->style_name, "$scheme://foo/bar.gif");
    $expected = "$scheme://styles/" . $this->style_name . "/$scheme/foo/bar.gif";
    $this->assertEqual($actual, $expected, 'Got the path for a file URI.');

    $actual = image_style_path($this->style_name, 'foo/bar.gif');
    $expected = "$scheme://styles/" . $this->style_name . "/$scheme/foo/bar.gif";
    $this->assertEqual($actual, $expected, 'Got the path for a relative file path.');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
