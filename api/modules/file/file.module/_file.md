# modules/file/file.module

- **Source:** [local](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · 1128 lines
- **Module/theme:** file

## File documentation

```text
@file
Defines a "managed_file" Form API field and a "file" field for Field module.
```

## Functions (derived index)

- [file_help()](file_help.md) — Implements hook_help().
- [file_menu()](file_menu.md) — Implements hook_menu().
- [file_element_info()](file_element_info.md) — Implements hook_element_info().
- [file_theme()](file_theme.md) — Implements hook_theme().
- [file_file_download()](file_file_download.md) — Implements hook_file_download().
- [file_ajax_upload()](file_ajax_upload.md) — Menu callback; Shared Ajax callback for file uploads and deletions.
- [file_ajax_progress()](file_ajax_progress.md) — Menu callback for upload progress.
- [file_progress_implementation()](file_progress_implementation.md) — Determines the preferred upload progress implementation.
- [file_file_delete()](file_file_delete.md) — Implements hook_file_delete().
- [file_managed_file_process()](file_managed_file_process.md) — Process function to expand the managed_file element type.
- [file_managed_file_value()](file_managed_file_value.md) — The #value_callback for a managed_file type element.
- [file_managed_file_validate()](file_managed_file_validate.md) — An #element_validate callback for the managed_file element.
- [file_managed_file_submit()](file_managed_file_submit.md) — Form submission handler for upload / remove buttons of managed_file elements.
- [file_managed_file_save_upload()](file_managed_file_save_upload.md) — Saves any files that have been uploaded into a managed_file element.
- [theme_file_managed_file()](theme_file_managed_file.md) — Returns HTML for a managed file element.
- [file_managed_file_pre_render()](file_managed_file_pre_render.md) — #pre_render callback to hide display of the upload or remove controls.
- [theme_file_link()](theme_file_link.md) — Returns HTML for a link to a file.
- [theme_file_icon()](theme_file_icon.md) — Returns HTML for an image with an appropriate icon for the given file.
- [file_icon_url()](file_icon_url.md) — Creates a URL to the icon for a file object.
- [file_icon_path()](file_icon_path.md) — Creates a path to the icon for a file object.
- [file_icon_map()](file_icon_map.md) — Determines the generic icon MIME package based on a file's MIME type.
- [file_get_file_references()](file_get_file_references.md) — Retrieves a list of references to a file.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
