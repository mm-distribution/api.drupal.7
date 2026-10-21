# image_style_form_submit()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 212–234 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L212-L234)
- **Module/theme:** image

## Signature

```php
function image_style_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for saving an image style.
```

## Code

```php
function image_style_form_submit($form, &$form_state) {
  // Update the image style.
  $style = $form_state['image_style'];
  $style['name'] = $form_state['values']['name'];
  $style['label'] = $form_state['values']['label'];

  // Update image effect weights.
  if (!empty($form_state['values']['effects'])) {
    foreach ($form_state['values']['effects'] as $ieid => $effect_data) {
      if (isset($style['effects'][$ieid])) {
        $effect = $style['effects'][$ieid];
        $effect['weight'] = $effect_data['weight'];
        image_effect_save($effect);
      }
    }
  }

  image_style_save($style);
  if ($form_state['values']['op'] == t('Update style')) {
    drupal_set_message(t('Changes to the style have been saved.'));
  }
  $form_state['redirect'] = 'admin/config/media/image-styles/edit/' . $style['name'];
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
