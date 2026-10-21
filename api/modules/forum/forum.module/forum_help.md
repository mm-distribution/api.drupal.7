# forum_help()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 11–52 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L11-L52)
- **Module/theme:** forum
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function forum_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function forum_help($path, $arg) {
  switch ($path) {
    case 'admin/help#forum':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Forum module lets you create threaded discussion forums with functionality similar to other message board systems. Forums are useful because they allow community members to discuss topics with one another while ensuring those conversations are archived for later reference. In a forum, users post topics and threads in nested hierarchies, allowing discussions to be categorized and grouped. The forum hierarchy consists of:') . '</p>';
      $output .= '<ul>';
      $output .= '<li>' . t('Optional containers (for example, <em>Support</em>), which can hold:') . '</li>';
      $output .= '<ul><li>' . t('Forums (for example, <em>Installing Drupal</em>), which can hold:') . '</li>';
      $output .= '<ul><li>' . t('Forum topics submitted by users (for example, <em>How to start a Drupal 6 Multisite</em>), which start discussions and are starting points for:') . '</li>';
      $output .= '<ul><li>' . t('Threaded comments submitted by users (for example, <em>You have these options...</em>).') . '</li>';
      $output .= '</ul>';
      $output .= '</ul>';
      $output .= '</ul>';
      $output .= '</ul>';
      $output .= '<p>' . t('For more information, see the online handbook entry for <a href="@forum">Forum module</a>.', array('@forum' => 'http://drupal.org/documentation/modules/forum')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Setting up forum structure') . '</dt>';
      $output .= '<dd>' . t('Visit the <a href="@forums">Forums page</a> to set up containers and forums to hold your discussion topics.', array('@forums' => url('admin/structure/forum'))) . '</dd>';
      $output .= '<dt>' . t('Starting a discussion') . '</dt>';
      $output .= '<dd>' . t('The <a href="@create-topic">Forum topic</a> link on the <a href="@content-add">Add new content</a> page creates the first post of a new threaded discussion, or thread.', array('@create-topic' => url('node/add/forum'), '@content-add' => url('node/add'))) . '</dd>';
      $output .= '<dt>' . t('Navigation') . '</dt>';
      $output .= '<dd>' . t('Enabling the Forum module provides a default <em>Forums</em> menu item in the navigation menu that links to the <a href="@forums">Forums page</a>.', array('@forums' => url('forum'))) . '</dd>';
      $output .= '<dt>' . t('Moving forum topics') . '</dt>';
      $output .= '<dd>' . t('A forum topic (and all of its comments) may be moved between forums by selecting a different forum while editing a forum topic. When moving a forum topic between forums, the <em>Leave shadow copy</em> option creates a link in the original forum pointing to the new location.') . '</dd>';
      $output .= '<dt>' . t('Locking and disabling comments') . '</dt>';
      $output .= '<dd>' . t('Selecting <em>Closed</em> under <em>Comment settings</em> while editing a forum topic will lock (prevent new comments on) the thread. Selecting <em>Hidden</em> under <em>Comment settings</em> while editing a forum topic will hide all existing comments on the thread, and prevent new ones.') . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/structure/forum':
      $output = '<p>' . t('Forums contain forum topics. Use containers to group related forums.') . '</p>';
      $output .= theme('more_help_link', array('url' => 'admin/help/forum'));
      return $output;
    case 'admin/structure/forum/add/container':
      return '<p>' . t('Use containers to group related forums.') . '</p>';
    case 'admin/structure/forum/add/forum':
      return '<p>' . t('A forum holds related forum topics.') . '</p>';
    case 'admin/structure/forum/settings':
      return '<p>' . t('Adjust the display of your forum topics. Organize the forums on the <a href="@forum-structure">forum structure page</a>.', array('@forum-structure' => url('admin/structure/forum'))) . '</p>';
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
