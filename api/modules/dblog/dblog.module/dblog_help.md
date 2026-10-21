# dblog_help()

- **Type:** Function
- **File:** [`modules/dblog/dblog.module`](_file.md), lines 17–34 · [local source](../../../../source/modules/dblog/dblog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module#L17-L34)
- **Module/theme:** dblog
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function dblog_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function dblog_help($path, $arg) {
  switch ($path) {
    case 'admin/help#dblog':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Database logging module logs system events in the Drupal database. For more information, see the online handbook entry for the <a href="@dblog">Database logging module</a>.', array('@dblog' => 'http://drupal.org/documentation/modules/dblog')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Monitoring your site') . '</dt>';
      $output .= '<dd>' . t('The Database logging module allows you to view an event log on the <a href="@dblog">Recent log messages</a> page. The log is a chronological list of recorded events containing usage data, performance data, errors, warnings and operational information. Administrators should check the log on a regular basis to ensure their site is working properly.', array('@dblog' => url('admin/reports/dblog'))) . '</dd>';
      $output .= '<dt>' . t('Debugging site problems') . '</dt>';
      $output .= '<dd>' . t('In case of errors or problems with the site, the <a href="@dblog">Recent log messages</a> page can be useful for debugging, since it shows the sequence of events. The log messages include usage information, warnings, and errors.', array('@dblog' => url('admin/reports/dblog'))) . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/reports/dblog':
      return '<p>' . t('The Database logging module monitors your website, capturing system events in a log (shown here) to be reviewed by an authorized individual at a later time. This log is a list of recorded events containing usage data, performance data, errors, warnings and operational information. It is vital to check the Recent log messages report on a regular basis, as it is often the only way to tell what is going on.') . '</p>';
  }
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.module](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
