# color_update_7001()

- **Type:** Function
- **File:** [`modules/color/color.install`](_file.md), lines 52–62 · [local source](../../../../source/modules/color/color.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.install#L52-L62)
- **Module/theme:** color
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function color_update_7001()
```

## Documentation

```text
Warn site administrator if unsafe CSS color codes are found in the database.
```

## Code

```php
function color_update_7001() {
  $theme_palettes = db_query("SELECT name FROM {variable} WHERE name LIKE 'color_%_palette'")->fetchCol();
  foreach ($theme_palettes as $name) {
    $palette = variable_get($name, array());
    foreach ($palette as $key => $color) {
      if (!preg_match('/^#([a-f0-9]{3}){1,2}$/iD', $color)) {
        drupal_set_message('Some of the custom CSS color codes specified via the color module are invalid. Please examine the themes which are making use of the color module at the <a href="'. url('admin/appearance/settings') .'">Appearance settings</a> page to verify their CSS color values.', 'warning');
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/color/color.install](https://github.com/drupal/drupal/blob/7.103/modules/color/color.install) · Licensed GPL-2.0-or-later (see LICENSE)._
