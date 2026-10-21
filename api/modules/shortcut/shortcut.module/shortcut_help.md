# shortcut_help()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 19–45 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L19-L45)
- **Module/theme:** shortcut
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function shortcut_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function shortcut_help($path, $arg) {
  global $user;

  switch ($path) {
    case 'admin/help#shortcut':
      $output = '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Shortcut module allows users to create sets of <em>shortcut</em> links to commonly-visited pages of the site. Shortcuts are contained within <em>sets</em>. Each user with <em>Select any shortcut set</em> permission can select a shortcut set created by anyone at the site. For more information, see the online handbook entry for <a href="@shortcut">Shortcut module</a>.', array('@shortcut' => 'http://drupal.org/documentation/modules/shortcut/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl><dt>' . t('Administering shortcuts') . '</dt>';
      $output .= '<dd>' . t('Users with the <em>Administer shortcuts</em> permission can manage shortcut sets and edit the shortcuts within sets from the <a href="@shortcuts">Shortcuts administration page</a>.', array('@shortcuts' => url('admin/config/user-interface/shortcut'))) . '</dd>';
      $output .= '<dt>' . t('Choosing shortcut sets') . '</dt>';
      $output .= '<dd>' . t('Users with permission to switch shortcut sets can choose a shortcut set to use from the Shortcuts tab of their user account page.') . '</dd>';
      $output .= '<dt>' . t('Adding and removing shortcuts') . '</dt>';
      $output .= '<dd>' . t('The Shortcut module creates an add/remove link for each page on your site; the link lets you add or remove the current page from the currently-enabled set of shortcuts (if your theme displays it and you have permission to edit your shortcut set). The core Seven administration theme displays this link next to the page title, as a small + or - sign. If you click on the + sign, you will add that page to your preferred set of shortcuts. If the page is already part of your shortcut set, the link will be a - sign, and will allow you to remove the current page from your shortcut set.') . '</dd>';
      $output .= '<dt>' . t('Displaying shortcuts') . '</dt>';
      $output .= '<dd>' . t('You can display your shortcuts by enabling the Shortcuts block on the <a href="@blocks">Blocks administration page</a>. Certain administrative modules also display your shortcuts; for example, the core <a href="@toolbar-help">Toolbar module</a> displays them near the top of the page, along with an <em>Edit shortcuts</em> link.', array('@blocks' => url('admin/structure/block'), '@toolbar-help' => url('admin/help/toolbar'))) . '</dd>';
      $output .= '</dl>';
      return $output;

    case 'admin/config/user-interface/shortcut':
    case 'admin/config/user-interface/shortcut/%':
      if (user_access('switch shortcut sets')) {
        $output = '<p>' . t('Define which shortcut set you are using on the <a href="@shortcut-link">Shortcuts tab</a> of your account page.', array('@shortcut-link' => url("user/{$user->uid}/shortcuts"))) . '</p>';
        return $output;
      }
  }
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
