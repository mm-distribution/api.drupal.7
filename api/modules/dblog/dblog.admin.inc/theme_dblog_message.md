# theme_dblog_message()

- **Type:** Function
- **File:** [`modules/dblog/dblog.admin.inc`](_file.md), lines 284–317 · [local source](../../../../source/modules/dblog/dblog.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc#L284-L317)
- **Module/theme:** dblog
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_dblog_message($variables)
```

## Documentation

```text
Returns HTML for a log message.

@param array $variables
  An associative array containing:
  - event: An object with at least the message and variables properties.
  - link: (optional) Format message as link, event->wid is required.

@ingroup themeable
```

## Code

```php
function theme_dblog_message($variables) {
  $output = '';
  $event = $variables['event'];
  // Check for required properties.
  if (isset($event->message) && isset($event->variables)) {
    $event_variables = @unserialize($event->variables);
    // Messages without variables or user specified text.
    if ($event_variables === NULL) {
      $output = $event->message;
    }
    elseif (!is_array($event_variables)) {
      $output = t('Log data is corrupted and cannot be unserialized: @message', array(
        '@message' => $event->message,
      ));
    }
    // Message to translate with injected variables.
    else {
      $output = t($event->message, $event_variables);
    }
    // If the output is expected to be a link, strip all the tags and
    // special characters by using filter_xss() without any allowed tags.
    // If not, use filter_xss_admin() to allow some tags.
    if ($variables['link'] && isset($event->wid)) {
      // Truncate message to 56 chars after stripping all the tags.
      $output = truncate_utf8(filter_xss($output, array()), 56, TRUE, TRUE);
      $output = l($output, 'admin/reports/event/' . $event->wid, array('html' => TRUE));
    }
    else {
      // Prevent XSS in log detail pages.
      $output = filter_xss_admin($output);
    }
  }
  return $output;
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
