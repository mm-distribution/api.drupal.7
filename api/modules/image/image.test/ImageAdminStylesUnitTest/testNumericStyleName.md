# ImageAdminStylesUnitTest::testNumericStyleName()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 613–624 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L613-L624)
- **Class:** [ImageAdminStylesUnitTest](../ImageAdminStylesUnitTest.md)
- **Module/theme:** image

## Signature

```php
function testNumericStyleName()
```

## Documentation

```text
Test creating an image style with a numeric name and ensuring it can be
applied to an image.
```

## Code

```php
  function testNumericStyleName() {
    $style_name = rand();
    $style_label = $this->randomString();
    $edit = array(
      'name' => $style_name,
      'label' => $style_label,
    );
    $this->drupalPost('admin/config/media/image-styles/add', $edit, t('Create new style'));
    $this->assertRaw(t('Style %name was created.', array('%name' => $style_label)), 'Image style successfully created.');
    $options = image_style_options();
    $this->assertTrue(array_key_exists($style_name, $options), format_string('Array key %key exists.', array('%key' => $style_name)));
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
