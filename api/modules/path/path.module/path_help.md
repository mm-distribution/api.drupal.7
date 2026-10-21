# path_help()

- **Type:** Function
- **File:** [`modules/path/path.module`](_file.md), lines 11–35 · [local source](../../../../source/modules/path/path.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module#L11-L35)
- **Module/theme:** path
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function path_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function path_help($path, $arg) {
  switch ($path) {
    case 'admin/help#path':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Path module allows you to specify an alias, or custom URL, for any existing internal system path. Aliases should not be confused with URL redirects, which allow you to forward a changed or inactive URL to a new URL. In addition to making URLs more readable, aliases also help search engines index content more effectively. Multiple aliases may be used for a single internal system path. To automate the aliasing of paths, you can install the contributed module <a href="@pathauto">Pathauto</a>. For more information, see the online handbook entry for the <a href="@path">Path module</a>.', array('@path' => 'http://drupal.org/documentation/modules/path', '@pathauto' => 'http://drupal.org/project/pathauto')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Creating aliases') . '</dt>';
      $output .= '<dd>' . t('Users with sufficient <a href="@permissions">permissions</a> can create aliases under the <em>URL path settings</em> section when they create or edit content. Some examples of aliases are: ', array('@permissions' => url('admin/people/permissions', array('fragment' => 'module-path'))));
      $output .= '<ul><li>' . t('<em>member/jane-smith</em> aliased to internal path <em>user/123</em>') . '</li>';
      $output .= '<li>' . t('<em>about-us/team</em> aliased to internal path <em>node/456</em>') . '</li>';
      $output .= '</ul></dd>';
      $output .= '<dt>' . t('Managing aliases') . '</dt>';
      $output .= '<dd>' . t('The Path module provides a way to search and view a <a href="@aliases">list of all aliases</a> that are in use on your website. Aliases can be added, edited and deleted through this list.', array('@aliases' => url('admin/config/search/path'))) . '</dd>';
      $output .= '</dl>';
      return $output;

    case 'admin/config/search/path':
      return '<p>' . t("An alias defines a different name for an existing URL path - for example, the alias 'about' for the URL path 'node/1'. A URL path can have multiple aliases.") . '</p>';

    case 'admin/config/search/path/add':
      return '<p>' . t('Enter the path you wish to create the alias for, followed by the name of the new alias.') . '</p>';
  }
}
```

---
_Drupal 7.103 · [modules/path/path.module](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module) · Licensed GPL-2.0-or-later (see LICENSE)._
