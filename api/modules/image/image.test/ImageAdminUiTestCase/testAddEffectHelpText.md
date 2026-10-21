# ImageAdminUiTestCase::testAddEffectHelpText()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 535–542 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L535-L542)
- **Class:** [ImageAdminUiTestCase](../ImageAdminUiTestCase.md)
- **Module/theme:** image

## Signature

```php
function testAddEffectHelpText()
```

## Documentation

```text
Test if the help text is available on the add effect form.
```

## Code

```php
  function testAddEffectHelpText() {
    // Create a random image style.
    $style = $this->createRandomStyle();

    // Open the add effect form and check for the help text.
    $this->drupalGet($style['path'] . '/add/image_crop');
    $this->assertText(t('Cropping will remove portions of an image to make it the specified dimensions.'), 'The image style effect help text was displayed on the add effect page.');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
