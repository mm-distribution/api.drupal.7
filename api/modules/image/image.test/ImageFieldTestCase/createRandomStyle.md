# ImageFieldTestCase::createRandomStyle()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 91–101 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L91-L101)
- **Class:** [ImageFieldTestCase](../ImageFieldTestCase.md)
- **Module/theme:** image

## Signature

```php
function createRandomStyle()
```

## Documentation

```text
Create a random style.

@return array
 A list containing the details of the generated image style.
```

## Code

```php
  function createRandomStyle() {
    $style_name = strtolower($this->randomName(10));
    $style_label = $this->randomString();
    image_style_save(array('name' => $style_name, 'label' => $style_label));
    $style_path = 'admin/config/media/image-styles/edit/' . $style_name;
    return array(
      'name' => $style_name,
      'label' => $style_label,
      'path' => $style_path,
    );
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
