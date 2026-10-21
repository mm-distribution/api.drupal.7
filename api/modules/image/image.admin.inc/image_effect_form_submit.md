# image_effect_form_submit()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 450–457 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L450-L457)
- **Module/theme:** image

## Signature

```php
function image_effect_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for updating an image effect.
```

## Code

```php
function image_effect_form_submit($form, &$form_state) {
  $style = $form_state['image_style'];
  $effect = array_merge($form_state['image_effect'], $form_state['values']);
  $effect['isid'] = $style['isid'];
  image_effect_save($effect);
  drupal_set_message(t('The image effect was successfully applied.'));
  $form_state['redirect'] = 'admin/config/media/image-styles/edit/' . $style['name'];
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
