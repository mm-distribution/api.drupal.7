# xmlrpc_date_get_xml()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 527–529 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L527-L529)

## Signature

```php
function xmlrpc_date_get_xml($xmlrpc_date)
```

## Documentation

```text
Converts an XML-RPC date-time object into XML.

@param $xmlrpc_date
  The XML-RPC date-time object.

@return string
  An XML representation of the date/time as XML.
```

## Code

```php
function xmlrpc_date_get_xml($xmlrpc_date) {
  return '<dateTime.iso8601>' . $xmlrpc_date->year . $xmlrpc_date->month . $xmlrpc_date->day . 'T' . $xmlrpc_date->hour . ':' . $xmlrpc_date->minute . ':' . $xmlrpc_date->second . '</dateTime.iso8601>';
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
