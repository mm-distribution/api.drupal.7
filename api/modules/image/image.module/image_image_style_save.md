# image_image_style_save()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 388–414 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L388-L414)
- **Module/theme:** image
- **Implements:** [hook_image_style_save()](../image.api.php/hook_image_style_save.md)

## Signature

```php
function image_image_style_save($style)
```

## Documentation

```text
Implements hook_image_style_save().
```

## Code

```php
function image_image_style_save($style) {
  if (isset($style['old_name']) && $style['old_name'] != $style['name']) {
    $instances = field_read_instances();
    // Loop through all fields searching for image fields.
    foreach ($instances as $instance) {
      if ($instance['widget']['module'] == 'image') {
        $instance_changed = FALSE;
        foreach ($instance['display'] as $view_mode => $display) {
          // Check if the formatter involves an image style.
          if ($display['type'] == 'image' && $display['settings']['image_style'] == $style['old_name']) {
            // Update display information for any instance using the image
            // style that was just deleted.
            $instance['display'][$view_mode]['settings']['image_style'] = $style['name'];
            $instance_changed = TRUE;
          }
        }
        if ($instance['widget']['settings']['preview_image_style'] == $style['old_name']) {
          $instance['widget']['settings']['preview_image_style'] = $style['name'];
          $instance_changed = TRUE;
        }
        if ($instance_changed) {
          field_update_instance($instance);
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
