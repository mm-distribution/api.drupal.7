# drupal_detect_baseurl()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 221–229 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L221-L229)

## Signature

```php
function drupal_detect_baseurl($file = 'install.php')
```

## Documentation

```text
Detects the base URL using the PHP $_SERVER variables.

@param $file
  The name of the file calling this function so we can strip it out of
  the URI when generating the base_url.

@return
  The auto-detected $base_url that should be configured in settings.php
```

## Code

```php
function drupal_detect_baseurl($file = 'install.php') {
  $proto = $_SERVER['HTTPS'] ? 'https://' : 'http://';
  $host = $_SERVER['SERVER_NAME'];
  $port = ($_SERVER['SERVER_PORT'] == 80 ? '' : ':' . $_SERVER['SERVER_PORT']);
  $uri = preg_replace("/\?.*/", '', $_SERVER['REQUEST_URI']);
  $dir = str_replace("/$file", '', $uri);

  return "$proto$host$port$dir";
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
