# image_style_delete_form_submit()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 349–355 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L349-L355)
- **Module/theme:** image

## Signature

```php
function image_style_delete_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler to delete an image style.
```

## Code

```php
function image_style_delete_form_submit($form, &$form_state) {
  $style = $form_state['image_style'];

  image_style_delete($style, $form_state['values']['replacement']);
  drupal_set_message(t('Style %name was deleted.', array('%name' => $style['label'])));
  $form_state['redirect'] = 'admin/config/media/image-styles';
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
