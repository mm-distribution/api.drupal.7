# image_style_revert_form()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 360–370 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L360-L370)
- **Module/theme:** image

## Signature

```php
function image_style_revert_form($form, &$form_state, $style)
```

## Documentation

```text
Confirmation form to revert a database style to its default.
```

## Code

```php
function image_style_revert_form($form, &$form_state, $style) {
  $form_state['image_style'] = $style;

  return confirm_form(
    $form,
    t('Revert the %style style?', array('%style' => $style['label'])),
    'admin/config/media/image-styles',
    t('Reverting this style will delete the customized settings and restore the defaults provided by the @module module.', array('@module' => $style['module'])),
    t('Revert'),  t('Cancel')
  );
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
