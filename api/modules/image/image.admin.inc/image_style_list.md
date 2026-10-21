# image_style_list()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 11–24 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L11-L24)
- **Module/theme:** image

## Signature

```php
function image_style_list()
```

## Documentation

```text
Menu callback; Listing of all current image styles.
```

## Code

```php
function image_style_list() {
  $page = array();

  $styles = image_styles();
  $page['image_style_list'] = array(
    '#markup' => theme('image_style_list', array('styles' => $styles)),
    '#attached' => array(
      'css' => array(drupal_get_path('module', 'image') . '/image.admin.css' => array()),
    ),
  );

  return $page;

}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
