# xmlrpc_server_output()

- **Type:** Function
- **File:** [`includes/xmlrpcs.inc`](_file.md), lines 126–132 · [local source](../../../source/includes/xmlrpcs.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc#L126-L132)

## Signature

```php
function xmlrpc_server_output($xml)
```

## Documentation

```text
Sends XML-RPC output to the browser.

@param string $xml
  XML to send to the browser.
```

## Code

```php
function xmlrpc_server_output($xml) {
  $xml = '<?xml version="1.0"?>' . "\n" . $xml;
  drupal_add_http_header('Content-Length', strlen($xml));
  drupal_add_http_header('Content-Type', 'text/xml');
  echo $xml;
  drupal_exit();
}
```

---
_Drupal 7.103 · [includes/xmlrpcs.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
