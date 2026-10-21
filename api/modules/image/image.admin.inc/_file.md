# modules/image/image.admin.inc

- **Source:** [local](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · 940 lines
- **Module/theme:** image

## File documentation

```text
@file
Administration pages for image settings.
```

## Functions (derived index)

- [image_style_list()](image_style_list.md) — Menu callback; Listing of all current image styles.
- [image_style_form()](image_style_form.md) — Form builder; Edit an image style name and effects order.
- [image_style_form_add_validate()](image_style_form_add_validate.md) — Validate handler for adding a new image effect to an image style.
- [image_style_form_add_submit()](image_style_form_add_submit.md) — Submit handler for adding a new image effect to an image style.
- [image_style_form_override_submit()](image_style_form_override_submit.md) — Submit handler for overriding a module-defined style.
- [image_style_form_submit()](image_style_form_submit.md) — Submit handler for saving an image style.
- [image_style_add_form()](image_style_add_form.md) — Form builder; Form for adding a new image style.
- [image_style_add_form_name_exists()](image_style_add_form_name_exists.md) — Check if the proposed machine name is already taken.
- [image_style_add_form_submit()](image_style_add_form_submit.md) — Submit handler for adding a new image style.
- [image_style_name_validate()](image_style_name_validate.md) — Element validate function to ensure unique, URL safe style names.
- [image_style_delete_form()](image_style_delete_form.md) — Form builder; Form for deleting an image style.
- [image_style_delete_form_submit()](image_style_delete_form_submit.md) — Submit handler to delete an image style.
- [image_style_revert_form()](image_style_revert_form.md) — Confirmation form to revert a database style to its default.
- [image_style_revert_form_submit()](image_style_revert_form_submit.md) — Submit handler to convert an overridden style to its default.
- [image_effect_form()](image_effect_form.md) — Form builder; Form for adding and editing image effects.
- [image_effect_form_submit()](image_effect_form_submit.md) — Submit handler for updating an image effect.
- [image_effect_delete_form()](image_effect_delete_form.md) — Form builder; Form for deleting an image effect.
- [image_effect_delete_form_submit()](image_effect_delete_form_submit.md) — Submit handler to delete an image effect.
- [image_effect_integer_validate()](image_effect_integer_validate.md) — Element validate handler to ensure an integer pixel value.
- [image_effect_color_validate()](image_effect_color_validate.md) — Element validate handler to ensure a hexadecimal color value.
- [image_effect_scale_validate()](image_effect_scale_validate.md) — Element validate handler to ensure that either a height or a width is specified.
- [image_resize_form()](image_resize_form.md) — Form structure for the image resize form.
- [image_scale_form()](image_scale_form.md) — Form structure for the image scale form.
- [image_crop_form()](image_crop_form.md) — Form structure for the image crop form.
- [image_rotate_form()](image_rotate_form.md) — Form structure for the image rotate form.
- [theme_image_style_list()](theme_image_style_list.md) — Returns HTML for the page containing the list of image styles.
- [theme_image_style_effects()](theme_image_style_effects.md) — Returns HTML for a listing of the effects within a specific image style.
- [theme_image_style_preview()](theme_image_style_preview.md) — Returns HTML for a preview of an image style.
- [theme_image_anchor()](theme_image_anchor.md) — Returns HTML for a 3x3 grid of checkboxes for image anchors.
- [theme_image_resize_summary()](theme_image_resize_summary.md) — Returns HTML for a summary of an image resize effect.
- [theme_image_scale_summary()](theme_image_scale_summary.md) — Returns HTML for a summary of an image scale effect.
- [theme_image_crop_summary()](theme_image_crop_summary.md) — Returns HTML for a summary of an image crop effect.
- [theme_image_rotate_summary()](theme_image_rotate_summary.md) — Returns HTML for a summary of an image rotate effect.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
