# theme_image_anchor()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 862–878 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L862-L878)
- **Module/theme:** image
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_image_anchor($variables)
```

## Documentation

```text
Returns HTML for a 3x3 grid of checkboxes for image anchors.

@param $variables
  An associative array containing:
  - element: A render element containing radio buttons.

@ingroup themeable
```

## Code

```php
function theme_image_anchor($variables) {
  $element = $variables['element'];

  $rows = array();
  $row = array();
  foreach (element_children($element) as $n => $key) {
    $element[$key]['#attributes']['title'] = $element[$key]['#title'];
    unset($element[$key]['#title']);
    $row[] = drupal_render($element[$key]);
    if ($n % 3 == 3 - 1) {
      $rows[] = $row;
      $row = array();
    }
  }

  return theme('table', array('header' => array(), 'rows' => $rows, 'attributes' => array('class' => array('image-anchor'))));
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
