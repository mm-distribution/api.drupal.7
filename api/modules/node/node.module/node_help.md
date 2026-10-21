# node_help()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 65–120 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L65-L120)
- **Module/theme:** node
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function node_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function node_help($path, $arg) {
  // Remind site administrators about the {node_access} table being flagged
  // for rebuild. We don't need to issue the message on the confirm form, or
  // while the rebuild is being processed.
  if ($path != 'admin/reports/status/rebuild' && $path != 'batch' && strpos($path, '#') === FALSE
      && user_access('access administration pages') && node_access_needs_rebuild()) {
    if ($path == 'admin/reports/status') {
      $message = t('The content access permissions need to be rebuilt.');
    }
    else {
      $message = t('The content access permissions need to be rebuilt. <a href="@node_access_rebuild">Rebuild permissions</a>.', array('@node_access_rebuild' => url('admin/reports/status/rebuild')));
    }
    drupal_set_message($message, 'error');
  }

  switch ($path) {
    case 'admin/help#node':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Node module manages the creation, editing, deletion, settings, and display of the main site content. Content items managed by the Node module are typically displayed as pages on your site, and include a title, some meta-data (author, creation time, content type, etc.), and optional fields containing text or other data (fields are managed by the <a href="@field">Field module</a>). For more information, see the online handbook entry for <a href="@node">Node module</a>.', array('@node' => 'http://drupal.org/documentation/modules/node', '@field' => url('admin/help/field'))) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Creating content') . '</dt>';
      $output .= '<dd>' . t('When new content is created, the Node module records basic information about the content, including the author, date of creation, and the <a href="@content-type">Content type</a>. It also manages the <em>publishing options</em>, which define whether or not the content is published, promoted to the front page of the site, and/or sticky at the top of content lists. Default settings can be configured for each <a href="@content-type">type of content</a> on your site.', array('@content-type' => url('admin/structure/types'))) . '</dd>';
      $output .= '<dt>' . t('Creating custom content types') . '</dt>';
      $output .= '<dd>' . t('The Node module gives users with the <em>Administer content types</em> permission the ability to <a href="@content-new">create new content types</a> in addition to the default ones already configured. Creating custom content types allows you the flexibility to add <a href="@field">fields</a> and configure default settings that suit the differing needs of various site content.', array('@content-new' => url('admin/structure/types/add'), '@field' => url('admin/help/field'))) . '</dd>';
      $output .= '<dt>' . t('Administering content') . '</dt>';
      $output .= '<dd>' . t('The <a href="@content">Content administration page</a> allows you to review and bulk manage your site content.', array('@content' => url('admin/content'))) . '</dd>';
      $output .= '<dt>' . t('Creating revisions') . '</dt>';
      $output .= '<dd>' . t('The Node module also enables you to create multiple versions of any content, and revert to older versions using the <em>Revision information</em> settings.') . '</dd>';
      $output .= '<dt>' . t('User permissions') . '</dt>';
      $output .= '<dd>' . t('The Node module makes a number of permissions available for each content type, which can be set by role on the <a href="@permissions">permissions page</a>.', array('@permissions' => url('admin/people/permissions', array('fragment' => 'module-node')))) . '</dd>';
      $output .= '</dl>';
      return $output;

    case 'admin/structure/types/add':
      return '<p>' . t('Individual content types can have different fields, behaviors, and permissions assigned to them.') . '</p>';

    case 'admin/structure/types/manage/%/display':
      return '<p>' . t('Content items can be displayed using different view modes: Teaser, Full content, Print, RSS, etc. <em>Teaser</em> is a short format that is typically used in lists of multiple content items. <em>Full content</em> is typically used when the content is displayed on its own page.') . '</p>' .
        '<p>' . t('Here, you can define which fields are shown and hidden when %type content is displayed in each view mode, and define how the fields are displayed in each view mode.', array('%type' => node_type_get_name($arg[4]))) . '</p>';

    case 'node/%/revisions':
      return '<p>' . t('Revisions allow you to track differences between multiple versions of your content, and revert back to older versions.') . '</p>';

    case 'node/%/edit':
      $node = node_load($arg[1]);
      $type = node_type_get_type($node);
      return (!empty($type->help) ? '<p>' . filter_xss_admin($type->help) . '</p>' : '');
  }

  if ($arg[0] == 'node' && $arg[1] == 'add' && $arg[2]) {
    $type = node_type_get_type(str_replace('-', '_', $arg[2]));
    return (!empty($type->help) ? '<p>' . filter_xss_admin($type->help) . '</p>' : '');
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
