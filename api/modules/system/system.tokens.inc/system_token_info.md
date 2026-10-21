# system_token_info()

- **Type:** Function
- **File:** [`modules/system/system.tokens.inc`](_file.md), lines 14–126 · [local source](../../../../source/modules/system/system.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tokens.inc#L14-L126)
- **Module/theme:** system
- **Implements:** [hook_token_info()](../system.api.php/hook_token_info.md)

## Signature

```php
function system_token_info()
```

## Documentation

```text
Implements hook_token_info().
```

## Code

```php
function system_token_info() {
  $types['site'] = array(
    'name' => t("Site information"),
    'description' => t("Tokens for site-wide settings and other global information."),
  );
  $types['date'] = array(
    'name' => t("Dates"),
    'description' => t("Tokens related to times and dates."),
  );
  $types['file'] = array(
    'name' => t("Files"),
    'description' => t("Tokens related to uploaded files."),
    'needs-data' => 'file',
  );

  // Site-wide global tokens.
  $site['name'] = array(
    'name' => t("Name"),
    'description' => t("The name of the site."),
  );
  $site['slogan'] = array(
    'name' => t("Slogan"),
    'description' => t("The slogan of the site."),
  );
  $site['mail'] = array(
    'name' => t("Email"),
    'description' => t("The administrative email address for the site."),
  );
  $site['url'] = array(
    'name' => t("URL"),
    'description' => t("The URL of the site's front page."),
  );
  $site['url-brief'] = array(
    'name' => t("URL (brief)"),
    'description' => t("The URL of the site's front page without the protocol."),
  );
  $site['login-url'] = array(
    'name' => t("Login page"),
    'description' => t("The URL of the site's login page."),
  );

  // Date related tokens.
  $date['short'] = array(
    'name' => t("Short format"),
    'description' => t("A date in 'short' format. (%date)", array('%date' => format_date(REQUEST_TIME, 'short'))),
  );
  $date['medium'] = array(
    'name' => t("Medium format"),
    'description' => t("A date in 'medium' format. (%date)", array('%date' => format_date(REQUEST_TIME, 'medium'))),
  );
  $date['long'] = array(
    'name' => t("Long format"),
    'description' => t("A date in 'long' format. (%date)", array('%date' => format_date(REQUEST_TIME, 'long'))),
  );
  $date['custom'] = array(
    'name' => t("Custom format"),
    'description' => t("A date in a custom format. See !php-date for details.", array('!php-date' => l(t('the PHP documentation'), 'http://php.net/manual/en/function.date.php'))),
  );
  $date['since'] = array(
    'name' => t("Time-since"),
    'description' => t("A date in 'time-since' format. (%date)", array('%date' => format_interval(REQUEST_TIME - 360, 2))),
  );
  $date['raw'] = array(
    'name' => t("Raw timestamp"),
    'description' => t("A date in UNIX timestamp format (%date)", array('%date' => REQUEST_TIME)),
  );


  // File related tokens.
  $file['fid'] = array(
    'name' => t("File ID"),
    'description' => t("The unique ID of the uploaded file."),
  );
  $file['name'] = array(
    'name' => t("File name"),
    'description' => t("The name of the file on disk."),
  );
  $file['path'] = array(
    'name' => t("Path"),
    'description' => t("The location of the file relative to Drupal root."),
  );
  $file['mime'] = array(
    'name' => t("MIME type"),
    'description' => t("The MIME type of the file."),
  );
  $file['size'] = array(
    'name' => t("File size"),
    'description' => t("The size of the file."),
  );
  $file['url'] = array(
    'name' => t("URL"),
    'description' => t("The web-accessible URL for the file."),
  );
  $file['timestamp'] = array(
    'name' => t("Timestamp"),
    'description' => t("The date the file was most recently changed."),
    'type' => 'date',
  );
  $file['owner'] = array(
    'name' => t("Owner"),
    'description' => t("The user who originally uploaded the file."),
    'type' => 'user',
  );

  return array(
    'types' => $types,
    'tokens' => array(
      'site' => $site,
      'date' => $date,
      'file' => $file,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/system/system.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
