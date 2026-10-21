# image_style_delete_form()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 326–344 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L326-L344)
- **Module/theme:** image
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function image_style_delete_form($form, &$form_state, $style)
```

## Documentation

```text
Form builder; Form for deleting an image style.

@param $style
  An image style array.

@ingroup forms
@see image_style_delete_form_submit()
```

## Code

```php
function image_style_delete_form($form, &$form_state, $style) {
  $form_state['image_style'] = $style;

  $replacement_styles = array_diff_key(image_style_options(TRUE, PASS_THROUGH), array($style['name'] => ''));
  $form['replacement'] = array(
    '#title' => t('Replacement style'),
    '#type' => 'select',
    '#options' => $replacement_styles,
    '#empty_option' => t('No replacement, just delete'),
  );

  return confirm_form(
    $form,
    t('Optionally select a style before deleting %style', array('%style' => $style['label'])),
    'admin/config/media/image-styles',
    t('If this style is in use on the site, you may select another style to replace it. All images that have been generated for this style will be permanently deleted.'),
    t('Delete'),  t('Cancel')
  );
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
