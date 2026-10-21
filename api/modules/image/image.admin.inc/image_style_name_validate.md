# image_style_name_validate()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 304–315 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L304-L315)
- **Module/theme:** image

## Signature

```php
function image_style_name_validate($element, $form_state)
```

## Documentation

```text
Element validate function to ensure unique, URL safe style names.

This function is no longer used in Drupal core since image style names are
now validated using #machine_name functionality. It is kept for backwards
compatibility (since non-core modules may be using it) and will be removed
in Drupal 8.
```

## Code

```php
function image_style_name_validate($element, $form_state) {
  // Check for duplicates.
  $styles = image_styles();
  if (isset($styles[$element['#value']]) && (!isset($form_state['image_style']['isid']) || $styles[$element['#value']]['isid'] != $form_state['image_style']['isid'])) {
    form_set_error($element['#name'], t('The image style name %name is already in use.', array('%name' => $element['#value'])));
  }

  // Check for illegal characters in image style names.
  if (preg_match('/[^0-9a-z_\-]/', $element['#value'])) {
    form_set_error($element['#name'], t('Please only use lowercase alphanumeric characters, underscores (_), and hyphens (-) for style names.'));
  }
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
