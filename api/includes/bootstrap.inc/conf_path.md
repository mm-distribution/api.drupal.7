# conf_path()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 561–592 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L561-L592)

## Signature

```php
function conf_path($require_settings = TRUE, $reset = FALSE)
```

## Documentation

```text
Returns the appropriate configuration directory.

Returns the configuration path based on the site's hostname, port, and
pathname. See default.settings.php for examples on how the URL is converted
to a directory.

@param bool $require_settings
  Only configuration directories with an existing settings.php file
  will be recognized. Defaults to TRUE. During initial installation,
  this is set to FALSE so that Drupal can detect a matching directory,
  then create a new settings.php file in it.
@param bool $reset
  Force a full search for matching directories even if one had been
  found previously. Defaults to FALSE.

@return
  The path of the matching directory.

@see default.settings.php
```

## Code

```php
function conf_path($require_settings = TRUE, $reset = FALSE) {
  $conf = &drupal_static(__FUNCTION__, '');

  if ($conf && !$reset) {
    return $conf;
  }

  $confdir = 'sites';

  $sites = array();
  if (file_exists(DRUPAL_ROOT . '/' . $confdir . '/sites.php')) {
    // This will overwrite $sites with the desired mappings.
    include(DRUPAL_ROOT . '/' . $confdir . '/sites.php');
  }

  $uri = explode('/', $_SERVER['SCRIPT_NAME'] ? $_SERVER['SCRIPT_NAME'] : $_SERVER['SCRIPT_FILENAME']);
  $server = explode('.', implode('.', array_reverse(explode(':', rtrim($_SERVER['HTTP_HOST'], '.')))));
  for ($i = count($uri) - 1; $i > 0; $i--) {
    for ($j = count($server); $j > 0; $j--) {
      $dir = implode('.', array_slice($server, -$j)) . implode('.', array_slice($uri, 0, $i));
      if (isset($sites[$dir]) && file_exists(DRUPAL_ROOT . '/' . $confdir . '/' . $sites[$dir])) {
        $dir = $sites[$dir];
      }
      if (file_exists(DRUPAL_ROOT . '/' . $confdir . '/' . $dir . '/settings.php') || (!$require_settings && file_exists(DRUPAL_ROOT . '/' . $confdir . '/' . $dir))) {
        $conf = "$confdir/$dir";
        return $conf;
      }
    }
  }
  $conf = "$confdir/default";
  return $conf;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
