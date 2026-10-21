# update_parse_db_url()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 863–885 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L863-L885)

## Signature

```php
function update_parse_db_url($db_url, $db_prefix)
```

## Documentation

```text
Parse pre-Drupal 7 database connection URLs and return D7 compatible array.

@return
  Drupal 7 DBTNG compatible array of database connection information.
```

## Code

```php
function update_parse_db_url($db_url, $db_prefix) {
  $databases = array();
  if (!is_array($db_url)) {
    $db_url = array('default' => $db_url);
  }
  foreach ($db_url as $database => $url) {
    $url = parse_url($url);
    $databases[$database]['default'] = array(
      // MySQLi uses the mysql driver.
      'driver' => $url['scheme'] == 'mysqli' ? 'mysql' : $url['scheme'],
      // Remove the leading slash to get the database name.
      'database' => substr(urldecode($url['path']), 1),
      'username' => urldecode($url['user']),
      'password' => isset($url['pass']) ? urldecode($url['pass']) : '',
      'host' => urldecode($url['host']),
      'port' => isset($url['port']) ? urldecode($url['port']) : '',
    );
    if (isset($db_prefix)) {
      $databases[$database]['default']['prefix'] = $db_prefix;
    }
  }
  return $databases;
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
