# update_results_page()

- **Type:** Function
- **File:** [`update.php`](_file.md), lines 160–239 · [local source](../../source/update.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/update.php#L160-L239)

## Signature

```php
function update_results_page()
```

## Documentation

```text
Displays results of the update script with any accompanying errors.
```

## Code

```php
function update_results_page() {
  drupal_set_title('Drupal database update');
  $links = update_helpful_links();

  update_task_list();
  // Report end result.
  if (module_exists('dblog') && user_access('access site reports')) {
    $log_message = ' All errors have been <a href="' . base_path() . '?q=admin/reports/dblog">logged</a>.';
  }
  else {
    $log_message = ' All errors have been logged.';
  }

  if ($_SESSION['update_success']) {
    $output = '<p>Updates were attempted. If you see no failures below, you may proceed happily back to your <a href="' . base_path() . '">site</a>. Otherwise, you may need to update your database manually.' . $log_message . '</p>';
  }
  else {
    $updates_remaining = reset($_SESSION['updates_remaining']);
    list($module, $version) = array_pop($updates_remaining);
    $output = '<p class="error">The update process was aborted prematurely while running <strong>update #' . $version . ' in ' . $module . '.module</strong>.' . $log_message;
    if (module_exists('dblog')) {
      $output .= ' You may need to check the <code>watchdog</code> database table manually.';
    }
    $output .= '</p>';
  }

  if (!empty($GLOBALS['update_free_access'])) {
    $output .= "<p><strong>Reminder: don't forget to set the <code>\$update_free_access</code> value in your <code>settings.php</code> file back to <code>FALSE</code>.</strong></p>";
  }

  $output .= theme('item_list', array('items' => $links));

  // Output a list of queries executed.
  if (!empty($_SESSION['update_results'])) {
    $all_messages = '';
    foreach ($_SESSION['update_results'] as $module => $updates) {
      if ($module != '#abort') {
        $module_has_message = FALSE;
        $query_messages = '';
        foreach ($updates as $number => $queries) {
          $messages = array();
          foreach ($queries as $query) {
            // If there is no message for this update, don't show anything.
            if (empty($query['query'])) {
              continue;
            }

            if ($query['success']) {
              $messages[] = '<li class="success">' . $query['query'] . '</li>';
            }
            else {
              $messages[] = '<li class="failure"><strong>Failed:</strong> ' . $query['query'] . '</li>';
            }
          }

          if ($messages) {
            $module_has_message = TRUE;
            $query_messages .= '<h4>Update #' . $number . "</h4>\n";
            $query_messages .= '<ul>' . implode("\n", $messages) . "</ul>\n";
          }
        }

        // If there were any messages in the queries then prefix them with the
        // module name and add it to the global message list.
        if ($module_has_message) {
          $all_messages .= '<h3>' . $module . " module</h3>\n" . $query_messages;
        }
      }
    }
    if ($all_messages) {
      $output .= '<div id="update-results"><h2>The following updates returned messages</h2>';
      $output .= $all_messages;
      $output .= '</div>';
    }
  }
  unset($_SESSION['update_results']);
  unset($_SESSION['update_success']);

  return $output;
}
```

---
_Drupal 7.103 · [update.php](https://github.com/drupal/drupal/blob/7.103/update.php) · Licensed GPL-2.0-or-later (see LICENSE)._
