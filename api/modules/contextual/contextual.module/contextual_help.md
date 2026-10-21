# contextual_help()

- **Type:** Function
- **File:** [`modules/contextual/contextual.module`](_file.md), lines 11–24 · [local source](../../../../source/modules/contextual/contextual.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.module#L11-L24)
- **Module/theme:** contextual
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function contextual_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function contextual_help($path, $arg) {
  switch ($path) {
    case 'admin/help#contextual':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Contextual links module displays links related to regions of pages on your site to users with <em>access contextual links</em> permission. For more information, see the online handbook entry for <a href="@contextual">Contextual links module</a>.', array('@contextual' => 'http://drupal.org/documentation/modules/contextual')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Displaying contextual links') . '</dt>';
      $output .= '<dd>' . t('Contextual links are supplied by modules, to give you quick access to tasks associated with regions of pages on your site. For instance, if you have a custom menu block displayed in a sidebar of your site, the Blocks and Menus modules will supply links to configure the block and edit the menu. The Contextual links module collects these links into a list for display by your theme, and also adds JavaScript code to the page to hide the links initially, and display them when your mouse hovers over the block.') . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/contextual/contextual.module](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.module) · Licensed GPL-2.0-or-later (see LICENSE)._
