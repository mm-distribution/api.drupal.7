# system_update_7046()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2482–2517 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2482-L2517)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7046()
```

## Documentation

```text
Switch from the Minnelli theme if it is the default or admin theme.
```

## Code

```php
function system_update_7046() {
  if (variable_get('theme_default') == 'minnelli' || variable_get('admin_theme') == 'minnelli') {
    // Make sure Garland is enabled.
    db_update('system')
      ->fields(array('status' => 1))
      ->condition('type', 'theme')
      ->condition('name', 'garland')
      ->execute();
    if (variable_get('theme_default') != 'garland') {
      // If the default theme isn't Garland, transfer all of Minnelli's old
      // settings to Garland.
      $settings = variable_get('theme_minnelli_settings', array());
      // Set the theme setting width to "fixed" to match Minnelli's old layout.
      $settings['garland_width'] = 'fixed';
      variable_set('theme_garland_settings', $settings);
      // Remove Garland's color files since they won't match Minnelli's.
      foreach (variable_get('color_garland_files', array()) as $file) {
        @drupal_unlink($file);
      }
      if (isset($file) && $file = dirname($file)) {
        @drupal_rmdir($file);
      }
      variable_del('color_garland_palette');
      variable_del('color_garland_stylesheets');
      variable_del('color_garland_logo');
      variable_del('color_garland_files');
      variable_del('color_garland_screenshot');
    }
    if (variable_get('theme_default') == 'minnelli') {
      variable_set('theme_default', 'garland');
    }
    if (variable_get('admin_theme') == 'minnelli') {
      variable_set('admin_theme', 'garland');
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
