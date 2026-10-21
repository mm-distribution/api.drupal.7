# poll_help()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 12–27 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L12-L27)
- **Module/theme:** poll
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function poll_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function poll_help($path, $arg) {
  switch ($path) {
    case 'admin/help#poll':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Poll module can be used to create simple surveys or questionnaires that display cumulative results. A poll is a good way to receive feedback from site users and community members. For more information, see the online handbook entry for the <a href="@poll">Poll module</a>.', array('@poll' => 'http://drupal.org/documentation/modules/poll/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Creating a poll') . '</dt>';
      $output .= '<dd>' . t('Users can create a poll by clicking on Poll on the <a href="@add-content">Add new content</a> page, and entering the question being posed, the answer choices, and beginning vote counts for each choice. The status (closed or active) and duration (length of time the poll remains active for new votes) can also be specified.', array('@add-content' => url('node/add'))) . '</dd>';
      $output .= '<dt>' . t('Viewing polls') . '</dt>';
      $output .= '<dd>' . t('You can visit the <a href="@poll">Polls</a> page to view all current polls, or alternately enable the <em>Most recent poll</em> block on the <a href="@blocks">Blocks administration page</a>. To vote in or view the results of a specific poll, you can click on the poll itself.', array('@poll' => url('poll'), '@blocks' => url('admin/structure/block'))) . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
