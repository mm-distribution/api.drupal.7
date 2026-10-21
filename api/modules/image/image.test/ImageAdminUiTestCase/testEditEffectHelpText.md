# ImageAdminUiTestCase::testEditEffectHelpText()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 547–565 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L547-L565)
- **Class:** [ImageAdminUiTestCase](../ImageAdminUiTestCase.md)
- **Module/theme:** image

## Signature

```php
function testEditEffectHelpText()
```

## Documentation

```text
Test if the help text is available on the edit effect form.
```

## Code

```php
  function testEditEffectHelpText() {
    // Create a random image style.
    $random_style = $this->createRandomStyle();

    // Add the crop effect to the image style.
    $edit = array();
    $edit['data[width]'] = 20;
    $edit['data[height]'] = 20;
    $this->drupalPost($random_style['path'] . '/add/image_crop', $edit, t('Add effect'));

    // Open the edit effect form and check for the help text.
    drupal_static_reset('image_styles');
    $style = image_style_load($random_style['name']);

    foreach ($style['effects'] as $ieid => $effect) {
      $this->drupalGet($random_style['path'] . '/effects/' . $ieid);
      $this->assertText(t('Cropping will remove portions of an image to make it the specified dimensions.'), 'The image style effect help text was displayed on the edit effect page.');
    }
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
