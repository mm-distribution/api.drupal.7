# modules/image/image.module

- **Source:** [local](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · 1495 lines
- **Module/theme:** image

## File documentation

```text
@file
Exposes global functionality for creating image styles.
```

## Functions (derived index)

- [image_help()](image_help.md) — Implements hook_help().
- [image_menu()](image_menu.md) — Implements hook_menu().
- [image_theme()](image_theme.md) — Implements hook_theme().
- [image_permission()](image_permission.md) — Implements hook_permission().
- [image_form_system_file_system_settings_alter()](image_form_system_file_system_settings_alter.md) — Implements hook_form_FORM_ID_alter().
- [image_system_file_system_settings_submit()](image_system_file_system_settings_submit.md) — Form submission handler for system_file_system_settings().
- [image_flush_caches()](image_flush_caches.md) — Implements hook_flush_caches().
- [image_file_download()](image_file_download.md) — Implements hook_file_download().
- [image_file_move()](image_file_move.md) — Implements hook_file_move().
- [image_file_delete()](image_file_delete.md) — Implements hook_file_delete().
- [image_image_default_styles()](image_image_default_styles.md) — Implements hook_image_default_styles().
- [image_image_style_save()](image_image_style_save.md) — Implements hook_image_style_save().
- [image_image_style_delete()](image_image_style_delete.md) — Implements hook_image_style_delete().
- [image_field_delete_field()](image_field_delete_field.md) — Implements hook_field_delete_field().
- [image_field_update_field()](image_field_update_field.md) — Implements hook_field_update_field().
- [image_field_delete_instance()](image_field_delete_instance.md) — Implements hook_field_delete_instance().
- [image_field_update_instance()](image_field_update_instance.md) — Implements hook_field_update_instance().
- [image_path_flush()](image_path_flush.md) — Clears cached versions of a specific file in all styles.
- [image_styles()](image_styles.md) — Gets an array of all styles and their settings.
- [image_style_load()](image_style_load.md) — Loads a style by style name or ID.
- [image_style_save()](image_style_save.md) — Saves an image style.
- [image_style_delete()](image_style_delete.md) — Deletes an image style.
- [image_style_effects()](image_style_effects.md) — Loads all the effects for an image style.
- [image_style_options()](image_style_options.md) — Gets an array of image styles suitable for using as select list options.
- [image_style_deliver()](image_style_deliver.md) — Page callback: Generates a derivative, given a style and image path.
- [_image_source_image_exists()](_image_source_image_exists.md) — Checks whether the provided source image exists.
- [image_style_create_derivative()](image_style_create_derivative.md) — Creates a new image derivative based on an image style.
- [image_style_transform_dimensions()](image_style_transform_dimensions.md) — Determines the dimensions of the styled image.
- [image_style_flush()](image_style_flush.md) — Flushes cached media for a style.
- [image_style_url()](image_style_url.md) — Returns the URL for an image derivative given a style and image path.
- [image_style_path_token()](image_style_path_token.md) — Generates a token to protect an image style derivative.
- [image_style_path()](image_style_path.md) — Returns the URI of an image when using a style.
- [image_default_style_save()](image_default_style_save.md) — Saves a default image style to the database.
- [image_default_style_revert()](image_default_style_revert.md) — Reverts the changes made by users to a default image style.
- [image_effect_definitions()](image_effect_definitions.md) — Returns a set of image effects.
- [image_effect_definition_load()](image_effect_definition_load.md) — Loads the definition for an image effect.
- [image_effects()](image_effects.md) — Loads all image effects from the database.
- [image_effect_load()](image_effect_load.md) — Loads a single image effect.
- [image_effect_save()](image_effect_save.md) — Saves an image effect.
- [image_effect_delete()](image_effect_delete.md) — Deletes an image effect.
- [image_effect_apply()](image_effect_apply.md) — Applies an image effect to the image object.
- [theme_image_style()](theme_image_style.md) — Returns HTML for an image using a specific image style.
- [image_filter_keyword()](image_filter_keyword.md) — Accepts a keyword (center, top, left, etc) and returns it as a pixel offset.
- [_image_effect_definitions_sort()](_image_effect_definitions_sort.md) — Internal function for sorting image effect definitions through uasort().

## Constants

### IMAGE_STORAGE_NORMAL

- Line 11

```php
define('IMAGE_STORAGE_NORMAL', 1);
```

```text
Image style constant for user presets in the database.
```

### IMAGE_STORAGE_OVERRIDE

- Line 16

```php
define('IMAGE_STORAGE_OVERRIDE', 2);
```

```text
Image style constant for user presets that override module-defined presets.
```

### IMAGE_STORAGE_DEFAULT

- Line 21

```php
define('IMAGE_STORAGE_DEFAULT', 4);
```

```text
Image style constant for module-defined presets in code.
```

### IMAGE_STORAGE_EDITABLE

- Line 26

```php
define('IMAGE_STORAGE_EDITABLE', IMAGE_STORAGE_NORMAL | IMAGE_STORAGE_OVERRIDE);
```

```text
Image style constant to represent an editable preset.
```

### IMAGE_STORAGE_MODULE

- Line 31

```php
define('IMAGE_STORAGE_MODULE', IMAGE_STORAGE_OVERRIDE | IMAGE_STORAGE_DEFAULT);
```

```text
Image style constant to represent any module-based preset.
```

### IMAGE_DERIVATIVE_TOKEN

- Line 36

```php
define('IMAGE_DERIVATIVE_TOKEN', 'itok');
```

```text
The name of the query parameter for image derivative tokens.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
