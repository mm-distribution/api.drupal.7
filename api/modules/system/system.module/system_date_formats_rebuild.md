# system_date_formats_rebuild()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3695–3710 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3695-L3710)
- **Module/theme:** system

## Signature

```php
function system_date_formats_rebuild()
```

## Documentation

```text
Resets the database cache of date formats and saves all new date formats.
```

## Code

```php
function system_date_formats_rebuild() {
  drupal_static_reset('system_get_date_formats');
  $date_formats = system_get_date_formats(NULL);

  foreach ($date_formats as $type => $formats) {
    foreach ($formats as $format => $info) {
      system_date_format_save($info);
    }
  }

  // Rebuild configured date formats locale list.
  drupal_static_reset('system_date_format_locale');
  system_date_format_locale();

  _system_date_formats_build();
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
