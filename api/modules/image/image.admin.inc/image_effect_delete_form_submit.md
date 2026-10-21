# image_effect_delete_form_submit()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 480–487 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L480-L487)
- **Module/theme:** image

## Signature

```php
function image_effect_delete_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler to delete an image effect.
```

## Code

```php
function image_effect_delete_form_submit($form, &$form_state) {
  $style = $form_state['image_style'];
  $effect = $form_state['image_effect'];

  image_effect_delete($effect);
  drupal_set_message(t('The image effect %name has been deleted.', array('%name' => $effect['label'])));
  $form_state['redirect'] = 'admin/config/media/image-styles/edit/' . $style['name'];
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
