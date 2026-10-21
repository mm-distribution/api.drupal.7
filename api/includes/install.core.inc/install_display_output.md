# install_display_output()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 698–726 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L698-L726)

## Signature

```php
function install_display_output($output, $install_state)
```

## Documentation

```text
Displays themed installer output and ends the page request.

Installation tasks should use drupal_set_title() to set the desired page
title, but otherwise this function takes care of theming the overall page
output during every step of the installation.

@param $output
  The content to display on the main part of the page.
@param $install_state
  An array of information about the current installation state.
```

## Code

```php
function install_display_output($output, $install_state) {
  drupal_page_header();

  // Prevent install.php from being indexed when installed in a sub folder.
  // robots.txt rules are not read if the site is within domain.com/subfolder
  // resulting in /subfolder/install.php being found through search engines.
  // When settings.php is writeable this can be used via an external database
  // leading a malicious user to gain php access to the server.
  $noindex_meta_tag = array(
    '#tag' => 'meta',
    '#attributes' => array(
      'name' => 'robots',
      'content' => 'noindex, nofollow',
    ),
  );
  drupal_add_html_head($noindex_meta_tag, 'install_meta_robots');

  // Only show the task list if there is an active task; otherwise, the page
  // request has ended before tasks have even been started, so there is nothing
  // meaningful to show.
  if (isset($install_state['active_task'])) {
    // Let the theming function know when every step of the installation has
    // been completed.
    $active_task = $install_state['installation_finished'] ? NULL : $install_state['active_task'];
    drupal_add_region_content('sidebar_first', theme('task_list', array('items' => install_tasks_to_display($install_state), 'active' => $active_task)));
  }
  print theme('install_page', array('content' => $output));
  exit;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
