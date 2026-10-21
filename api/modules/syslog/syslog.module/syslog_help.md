# syslog_help()

- **Type:** Function
- **File:** [`modules/syslog/syslog.module`](_file.md), lines 27–42 · [local source](../../../../source/modules/syslog/syslog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.module#L27-L42)
- **Module/theme:** syslog
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function syslog_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function syslog_help($path, $arg) {
  switch ($path) {
    case 'admin/help#syslog':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t("The Syslog module logs events by sending messages to the logging facility of your web server's operating system. Syslog is an operating system administrative logging tool that provides valuable information for use in system management and security auditing. Most suited to medium and large sites, Syslog provides filtering tools that allow messages to be routed by type and severity. For more information, see the online handbook entry for <a href='@syslog'>Syslog module</a> and PHP's <a href='@php_openlog'>openlog</a> and <a href='@php_syslog'>syslog</a> functions.", array('@syslog' => 'http://drupal.org/documentation/modules/syslog', '@php_openlog' => 'http://www.php.net/manual/function.openlog.php', '@php_syslog' => 'http://www.php.net/manual/function.syslog.php')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Logging for UNIX, Linux, and Mac OS X') . '</dt>';
      $output .= '<dd>' . t('On UNIX, Linux, and Mac OS X, the file <em>/etc/syslog.conf</em> defines the routing configuration. Messages can be flagged with the codes <code>LOG_LOCAL0</code> through <code>LOG_LOCAL7</code>. For information on Syslog facilities, severity levels, and how to set up <em>syslog.conf</em>, see the <em>syslog.conf</em> manual page on your command line.') . '</dd>';
      $output .= '<dt>' . t('Logging for Microsoft Windows') . '</dt>';
      $output .= '<dd>' . t('On Microsoft Windows, messages are always sent to the Event Log using the code <code>LOG_USER</code>.') . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/syslog/syslog.module](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
