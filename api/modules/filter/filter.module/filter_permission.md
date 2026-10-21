# filter_permission()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 348–368 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L348-L368)
- **Module/theme:** filter
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function filter_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function filter_permission() {
  $perms['administer filters'] = array(
    'title' => t('Administer text formats and filters'),
    'description' => t('Define how text is handled by combining filters into <a href="@url">text formats</a>.', array('@url' => url('admin/config/content/formats'))),
    'restrict access' => TRUE,
  );

  // Generate permissions for each text format. Warn the administrator that any
  // of them are potentially unsafe.
  foreach (filter_formats() as $format) {
    $permission = filter_permission_name($format);
    if (!empty($permission)) {
      $format_name_replacement = l($format->name, 'admin/config/content/formats/' . $format->format);
      $perms[$permission] = array(
        'title' => t("Use the !text_format text format", array('!text_format' => $format_name_replacement,)),
        'description' => drupal_placeholder(t('Warning: This permission may have security implications depending on how the text format is configured.')),
      );
    }
  }
  return $perms;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
