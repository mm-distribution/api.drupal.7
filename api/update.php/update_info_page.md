# update_info_page()

- **Type:** Function
- **File:** [`update.php`](_file.md), lines 250–273 · [local source](../../source/update.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/update.php#L250-L273)

## Signature

```php
function update_info_page()
```

## Documentation

```text
Provides an overview of the Drupal database update.

This page provides cautionary suggestions that should happen before
proceeding with the update to ensure data integrity.

@return
  Rendered HTML form.
```

## Code

```php
function update_info_page() {
  // Change query-strings on css/js files to enforce reload for all users.
  _drupal_flush_css_js();
  // Flush the cache of all data for the update status module.
  if (db_table_exists('cache_update')) {
    cache_clear_all('*', 'cache_update', TRUE);
  }

  update_task_list('info');
  drupal_set_title('Drupal database update');
  $token = drupal_get_token('update');
  $output = '<p>Use this utility to update your database whenever a new release of Drupal or a module is installed.</p><p>For more detailed information, see the <a href="http://drupal.org/upgrade">upgrading handbook</a>. If you are unsure what these terms mean you should probably contact your hosting provider.</p>';
  $output .= "<ol>\n";
  $output .= "<li><strong>Back up your code</strong>. Hint: when backing up module code, do not leave that backup in the 'modules' or 'sites/*/modules' directories as this may confuse Drupal's auto-discovery mechanism.</li>\n";
  $output .= '<li>Put your site into <a href="' . base_path() . '?q=admin/config/development/maintenance">maintenance mode</a>.</li>' . "\n";
  $output .= "<li><strong>Back up your database</strong>. This process will change your database values and in case of emergency you may need to revert to a backup.</li>\n";
  $output .= "<li>Install your new files in the appropriate location, as described in the handbook.</li>\n";
  $output .= "</ol>\n";
  $output .= "<p>When you have performed the steps above, you may proceed.</p>\n";
  $form_action = check_url(drupal_current_script_url(array('op' => 'selection', 'token' => $token)));
  $output .= '<form method="post" action="' . $form_action . '"><p><input type="submit" value="Continue" class="form-submit" /></p></form>';
  $output .= "\n";
  return $output;
}
```

---
_Drupal 7.103 · [update.php](https://github.com/drupal/drupal/blob/7.103/update.php) · Licensed GPL-2.0-or-later (see LICENSE)._
