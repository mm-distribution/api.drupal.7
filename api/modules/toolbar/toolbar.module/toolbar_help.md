# toolbar_help()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 11–23 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L11-L23)
- **Module/theme:** toolbar
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function toolbar_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function toolbar_help($path, $arg) {
  switch ($path) {
    case 'admin/help#toolbar':
      $output = '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Toolbar module displays links to top-level administration menu items and links from other modules at the top of the screen. For more information, see the online handbook entry for <a href="@toolbar">Toolbar module</a>.', array('@toolbar' => 'http://drupal.org/documentation/modules/toolbar/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Displaying administrative links') . '</dt>';
      $output .= '<dd>' . t('The Toolbar module displays a bar containing top-level administrative links across the top of the screen. Below that, the Toolbar module has a <em>drawer</em> section where it displays links provided by other modules, such as the core <a href="@shortcuts-help">Shortcut module</a>. The drawer can be hidden/shown by using the show/hide shortcuts link at the end of the toolbar.', array('@shortcuts-help' => url('admin/help/shortcut'))) . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
