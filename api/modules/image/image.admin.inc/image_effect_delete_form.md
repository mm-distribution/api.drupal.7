# image_effect_delete_form()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 469–475 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L469-L475)
- **Module/theme:** image
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function image_effect_delete_form($form, &$form_state, $style, $effect)
```

## Documentation

```text
Form builder; Form for deleting an image effect.

@param $style
  Name of the image style from which the image effect will be removed.
@param $effect
  Name of the image effect to remove.
@ingroup forms
@see image_effect_delete_form_submit()
```

## Code

```php
function image_effect_delete_form($form, &$form_state, $style, $effect) {
  $form_state['image_style'] = $style;
  $form_state['image_effect'] = $effect;

  $question = t('Are you sure you want to delete the @effect effect from the %style style?', array('%style' => $style['label'], '@effect' => $effect['label']));
  return confirm_form($form, $question, 'admin/config/media/image-styles/edit/' . $style['name'], '', t('Delete'));
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
