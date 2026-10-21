# color_help()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 10–23 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L10-L23)
- **Module/theme:** color
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function color_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function color_help($path, $arg) {
  switch ($path) {
    case 'admin/help#color':
      $output = '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Color module allows users with the <em>Administer site configuration</em> permission to quickly and easily change the color scheme of themes that have been built to be compatible with it. For more information, see the online handbook entry for <a href="@color">Color module</a>.', array('@color' => 'http://drupal.org/documentation/modules/color')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Changing colors') . '</dt>';
      $output .= '<dd>' . t("Using the Color module allows you to easily change the color of links, backgrounds, text, and other theme elements. To change the color settings for a compatible theme, select the <em>Settings</em> link for your theme on the <a href='@configure'>Themes administration page</a>. If you don't see a color picker on that page, then your theme is not compatible with the color module. If you are sure that the theme does indeed support the color module, but the color picker does not appear, then <a href='@troubleshoot'>follow these troubleshooting procedures</a>.", array('@configure' => url('admin/appearance'), '@troubleshoot' => 'http://drupal.org/node/109457')) . '</dd>';
      $output .= '<dd>' . t("The Color module saves a modified copy of the theme's specified stylesheets in the files directory. This means that if you make any manual changes to your theme's stylesheet, <em>you must save your color settings again, even if they haven't changed</em>. This step is required because the module stylesheets (in the files directory) need to be recreated to include your changes.") . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
