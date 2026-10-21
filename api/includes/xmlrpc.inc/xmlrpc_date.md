# xmlrpc_date()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 492–516 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L492-L516)

## Signature

```php
function xmlrpc_date($time)
```

## Documentation

```text
Converts a PHP or ISO date/time to an XML-RPC object.

@param $time
  A PHP timestamp or an ISO date-time string.

@return object
  An XML-RPC time/date object.
```

## Code

```php
function xmlrpc_date($time) {
  $xmlrpc_date = new stdClass();
  $xmlrpc_date->is_date = TRUE;
  // $time can be a PHP timestamp or an ISO one
  if (is_numeric($time)) {
    $xmlrpc_date->year = gmdate('Y', $time);
    $xmlrpc_date->month = gmdate('m', $time);
    $xmlrpc_date->day = gmdate('d', $time);
    $xmlrpc_date->hour = gmdate('H', $time);
    $xmlrpc_date->minute = gmdate('i', $time);
    $xmlrpc_date->second = gmdate('s', $time);
    $xmlrpc_date->iso8601 = gmdate('Ymd\TH:i:s', $time);
  }
  else {
    $xmlrpc_date->iso8601 = $time;
    $time = str_replace(array('-', ':'), '', $time);
    $xmlrpc_date->year = substr($time, 0, 4);
    $xmlrpc_date->month = substr($time, 4, 2);
    $xmlrpc_date->day = substr($time, 6, 2);
    $xmlrpc_date->hour = substr($time, 9, 2);
    $xmlrpc_date->minute = substr($time, 11, 2);
    $xmlrpc_date->second = substr($time, 13, 2);
  }
  return $xmlrpc_date;
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
